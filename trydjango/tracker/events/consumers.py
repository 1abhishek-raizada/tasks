import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EventConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("events",self.channel_name)
        print('connected webs')

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("events",self.channel_name)
        print('webs disconnected')
    async def send_event(self,event):
        
        await self.send(text_data=json.dumps({"message" : event["message"]}))    


















        