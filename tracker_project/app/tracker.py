from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import requests
import time


#function to send tracked activity to fastapi
def track_activity(activity_type,employee_id,status="active"):
    url="http://127.0.0.1:8000/track_activity"
    data={
        "employee_id":employee_id,                    #will replace it with actual employee_id
        "activity_type":activity_type,      
        "status":status                   #update to inactive after 5 minutes of inactivity
    }
    try:
        response=requests.post(url,json=data)
        if response.status_code==200:
            print(f"Activity for employee {employee_id} tracked successfully")
        else:
            print(f"Failed to track activity: {response.status_code},{response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error in sending request: {e}")            

#Mouse activity listener
def on_click(x,y,button,pressed):
    if pressed:
        track_activity("click")

#Keyboard activity listener
def on_press(key):
    track_activity("keyboard")

#Listen for mouse clicks and keyboard presses
with MouseListener(on_click=on_click) as mouse_listener,KeyboardListener(on_press=on_press) as keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()            
    