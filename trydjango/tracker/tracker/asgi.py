"""
ASGI config for tracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import events.routing



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracker.settings')

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket":URLRouter(events.routing.websocket_urlpatterns),
})
