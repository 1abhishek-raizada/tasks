from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pynput import keyboard, mouse
from datetime import datetime, timedelta
from app import models, database, auth
import threading
import pytz
from app.utils.email_alert import send



IST=pytz.timezone("Asia/Kolkata")
def get_current_time():
    return datetime.now(IST)

# Dictionary to keep track of active listeners per user
active_listeners = {}
inactive_timers = {}

INACTIVITY_LIMIT = 180  # 3 minutes






def log_activity(action: str, db: Session, employee_id: int):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not employee:
        return

    now = get_current_time()
    employee.is_active = True
    employee.last_active = now 

    working_hours = db.query(models.WorkingHours).filter(
        models.WorkingHours.employee_id == employee_id
    ).first()

    if not working_hours:
        working_hours = models.WorkingHours(
            employee_id=employee_id,
            total_active_seconds=0.0,
            last_active_time=now
        )
        db.add(working_hours)
        db.commit()
    else:
        last_active=IST.localize(working_hours.last_active_time) if working_hours.last_active_time.tzinfo is None else working_hours.last_active_time
        time_diff = (now - last_active).total_seconds()

        #Capping the time diff to avoid logging huge gaps
        if 5 < time_diff < INACTIVITY_LIMIT + 10:
            working_hours.total_active_seconds += time_diff

            today = now.date()
            daily_hours = db.query(models.DailyWorkingHours).filter_by(
                employee_id=employee_id, date=today
            ).first()

            if not daily_hours:
                daily_hours = models.DailyWorkingHours(
                    employee_id=employee_id,
                    date=today,
                    total_active_seconds=0.0
                )
                db.add(daily_hours)

            daily_hours.total_active_seconds += time_diff

        working_hours.last_active_time = now

            #  Reset the alert flag if user becomes active again
        if working_hours.inactivity_alert_sent:
            working_hours.inactivity_alert_sent = False


    new_activity = models.ActivityLog(
        employee_id=employee_id,
        action=action,
        timestamp=now
    )
    db.add(new_activity)
    db.commit()

    reset_inactivity_timer(db, employee_id)



def reset_inactivity_timer(db, employee_id):
    if employee_id in inactive_timers:
        inactive_timers[employee_id].cancel()

    timer = threading.Timer(INACTIVITY_LIMIT, mark_inactive, args=[employee_id])
    inactive_timers[employee_id] = timer
    timer.start()    


def mark_inactive(employee_id: int):
    with next(database.get_db()) as db:
        employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
        if employee:
            employee.is_active = False

            working_hours=db.query(models.WorkingHours).filter_by(employee_id=employee_id).first()
            if working_hours and not working_hours.inactivity_alert_sent:
                #sending alert
                send_inactivity_alert(employee.username)
                working_hours.inactivity_alert_sent=True
                db.add(working_hours)

            db.commit()
            stop_tracking(employee.username)
            detect_reactivation(employee.username)

def detect_reactivation(username):
    def on_event(_):
        restart_tracking(username)
        return False

    keyboard.Listener(on_press=on_event).start()
    mouse.Listener(on_click=on_event).start()

def restart_tracking(username):
    if username in active_listeners:
        return

    with next(database.get_db()) as db:
        employee = db.query(models.Employee).filter(models.Employee.username == username).first()
        if not employee:
            return

        stop_tracking(username)

        def on_event(event_type: str):
            log_activity(event_type, db, employee.id)

        keyboard_listener = keyboard.Listener(on_press=lambda _: on_event("keyboard"))
        mouse_listener = mouse.Listener(on_click=lambda _: on_event("mouse"))

        keyboard_listener.start()
        mouse_listener.start()

        active_listeners[username] = (keyboard_listener, mouse_listener)
        reset_inactivity_timer(db, employee.id)


def stop_tracking(username):
    if username in active_listeners:
        keyboard_listener, mouse_listener = active_listeners[username]
        keyboard_listener.stop()
        mouse_listener.stop()
        del active_listeners[username]

    with next(database.get_db()) as db:
        employee = db.query(models.Employee).filter(models.Employee.username == username).first()
        if employee and employee.id in inactive_timers:
            inactive_timers[employee.id].cancel()
            del inactive_timers[employee.id]      


def log(message):
    print(f"[LOG] {datetime.now()}: {message}")              



def send_inactivity_alert(username: str):
    with next(database.get_db()) as db:
        employee = db.query(models.Employee).filter_by(username=username).first()
        if employee and employee.email:
            subject = "⚠️ Inactivity Alert"
            body = f"""
Hi {username},

We've noticed you've been inactive for over 3 minutes.

Please resume your work or reach out if there's an issue.

Thanks,  
The Tracker Bot 📉
"""
            send(employee.email, subject, body)
        else:
            print(f"Alert: {username} inactive, but no email is available.")

