# network_analysis_tool/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, ChannelNameRouter
from traffic.consumers import PacketCaptureConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'network_analysis_tool.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "channel": ChannelNameRouter({
        "capture-packets": PacketCaptureConsumer.as_asgi(),
    }),
})
