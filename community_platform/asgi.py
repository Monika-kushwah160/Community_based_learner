import os
import django

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack

import community_platform.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "community_platform.settings")

django.setup()

application = ProtocolTypeRouter({

    "http": get_asgi_application(),

    "websocket": AuthMiddlewareStack(
        URLRouter(
            community_platform.routing.websocket_urlpatterns
        )
    ),

})