from channels.routing import ProtocolTypeRouter, ChannelNameRouter
from traffic.consumers import PacketCaptureConsumer

application = ProtocolTypeRouter({
    "channel": ChannelNameRouter({
        "capture-packets": PacketCaptureConsumer,
    }),
})
