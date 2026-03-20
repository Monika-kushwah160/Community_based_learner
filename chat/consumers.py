import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from .models import ChatMessage
from sessions_app.models import Session

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.session_id = self.scope["url_route"]["kwargs"]["session_id"]

        self.room_group_name = f"chat_{self.session_id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):

        data = json.loads(text_data)

        message = data["message"]

        user = self.scope["user"]

        session = await Session.objects.aget(id=self.session_id)

        await ChatMessage.objects.acreate(
            session=session,
            user=user,
            message=message
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": user.username
            }
        )

    async def chat_message(self, event):

        await self.send(text_data=json.dumps({
            "message": event["message"],
            "username": event["username"]
        }))