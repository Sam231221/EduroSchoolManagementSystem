## 📖 In settings.py

```
INSTALLED_APPS = [
    'channels',
    'MChat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

ASGI_APPLICATION = 'Apractice.routing.application'

#Use this for development only
CHANNEL_LAYERS = {
    'default': {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

#Use this for Production
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        }
    }
}

```

## 📖 In app/consumers.py

```
from channels.generic.websocket import AsyncConsumer
from channels.exceptions import StopConsumer
class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_recieve(self, event):
        await self.send({
            "type": "websocket.send",
        })

    async def websocket_disconnect(self, event):
        print('Disconnected:', event)
        raise StopConsumer()
```

## 📖 In app/routing.py

```
from django.urls import re_path
from . import consumers
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
```
