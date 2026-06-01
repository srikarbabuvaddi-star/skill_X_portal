import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        payload = json.loads(text_data)
        message = payload['message']
        username = payload['username']

    
        await self.persist_message_to_db(username, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'msg',
                'message': message,
                'username': username
            }
        )

    async def msg(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username']
        }))

    
    @database_sync_to_async
    def persist_message_to_db(self, username, message):
        
        from django.contrib.auth.models import User
        from .models import SavedMessage, MessagingRoom
        
        try:
            user = User.objects.get(username=username)
            room, _ = MessagingRoom.objects.get_or_create(room_token=self.room_name)
            SavedMessage.objects.create(room=room, author=user, content=message)
        except Exception as e:
            print(f"Database write bypass log: {e}")