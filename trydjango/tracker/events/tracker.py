from pynput import keyboard,mouse
from channels.layers import get_channel_layer
import asyncio
import time,json



def send_event(event):
    try:
        event_data=json.loads(event)
    except json.JSONDecodeError:
        event_data=None
    if event_data and "status" in event_data:
        message=json.dumps(event_data)
    else:
        if "[Keyboard]" in event:
            event_type="Keyboard"
            key_or_button=event.split("] ")[1]
            x,y=None,None
        elif "[Mouse]" in event:
            event_type="Mouse"
            parts=event.split(" ")
            key_or_button=parts[1]
            
        else:
            event_type,key_or_button="Unknown",event

        event_data={
            "type":event_type,
            "key":key_or_button,
            

        }   
        message=json.dumps(event_data)             

            
                    






    from .models import Event
   
    

    Event.objects.create(event_type=event_type,key_or_button=key_or_button)        
    channel_layer=get_channel_layer()
    #print('sending event to websocket: {event}')
    asyncio.run(channel_layer.group_send (
        "events",
        {"type" : "send_event","message":message}
    ))

def on_key_press(key):
    try:
        key_name=key.char       #for normal keys
    except AttributeError:
        key_name=str(key)       #for special keys
    event=f"[Keyboard] {key_name} pressed"
    send_event(event)
    

def on_key_release(key):
    if key == keyboard.Key.esc:
        event=("[Keyboard] ESC pressed. Stopping....")
        send_event(event)
        return False

def on_click(x,y,button,pressed):
    
    event_type="Pressed" if pressed else "Released"
    #print('clicked')
    event=f"[Mouse] {button} {event_type} at ({x},{y})"
    send_event(event) 



    
last_activity_time=0
def on_move(x,y):
    global last_activity_time
    current_time=time.time()
    if current_time - last_activity_time > 5:
        last_activity_time =current_time
        print('user is active(Mouse Moved)')
        event_data={"status":"active"}
        channel_layer=get_channel_layer()
        asyncio.run(channel_layer.group_send(
            "events",
            {"type":"send_event","message": json.dumps(event_data)}
        ))
                  

def start_listeners():  
    print('tracker has started here')
    keyboard_listener=keyboard.Listener(on_press=on_key_press,on_release=on_key_release)  
    mouse_listener=mouse.Listener(on_click=on_click,on_move=on_move)

    keyboard_listener.start()
    mouse_listener.start()

    keyboard_listener.join()
    mouse_listener.stop()