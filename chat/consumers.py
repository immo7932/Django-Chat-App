from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # The URL contains the ID of the other user you want to chat with.
        self.other_user_id = int(self.scope['url_route']['kwargs']['user_id'])
        self.current_user_id = self.scope['user'].id

        # Compute a unique room name that is the same for both users,
        # for example "chat_3_5" (smaller ID comes first)
        room_ids = sorted([self.current_user_id, self.other_user_id])
        self.room_name = f"chat_{room_ids[0]}_{room_ids[1]}"

        # Add this connection to the channel group for this room.
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()
        print(f"Connection accepted to room: {self.room_name}")

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )
        print(f"Disconnected from room: {self.room_name}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')
        sender = self.scope['user']

        # Save the message to the database.
        await self.save_message(sender, self.other_user_id, message)

        # Broadcast the message to everyone in the room.
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_username': sender.username,
            }
        )

    async def chat_message(self, event):
        # Called when someone has sent a message to the group.
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender_username': event['sender_username'],
        }))

    @sync_to_async
    def save_message(self, sender, receiver_id, message):
        receiver = User.objects.get(id=receiver_id)
        Message.objects.create(sender=sender, receiver=receiver, content=message)
