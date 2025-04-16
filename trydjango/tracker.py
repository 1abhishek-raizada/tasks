from pynput import keyboard,mouse
#import pandas as pd
import sqlite3
import time

LOG_FILE='activity_log.txt'
stop_listening=False

def log_event(event):
    timestamp=time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE,"a") as f:
        f.write(f"{timestamp} - {event}\n")




def on_key_press(key):
    try:
        key_name=key.char       #for normal keys
    except AttributeError:
        key_name=str(key)       #for special keys
    print(f"[Keyboard] {key_name} pressed")
    log_event(f"[Keyboard] {key_name} pressed")
    

def on_key_release(key):
    if key == keyboard.Key.esc:
        print("[Keyboard] ESC pressed. Stopping....")
        log_event("[Keyboard] ESC pressed. Stopping....")
        stop_listening=True
        return False

def on_click(x,y,button,pressed):
    if stop_listening:
        return False
    event_type="Pressed" if pressed else "Released"
    print(f"[Mouse] {button} {event_type} at ({x},{y})")
    log_event(f"[Mouse] {button} {event_type} at ({x},{y})") 

def on_move(x,y):
    if stop_listening:
        return False
    print(f"[Mouse] Moved to ({x},{y})")
    log_event(f"[Mouse] Moved to ({x},{y})")               
  
keyboard_listener=keyboard.Listener(on_press=on_key_press,on_release=on_key_release)  
mouse_listener=mouse.Listener(on_click=on_click,on_move=on_move)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.stop()