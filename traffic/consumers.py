# traffic/consumers.py

import pyshark
from channels.generic.base import AsyncConsumer
import asyncio

class PacketCaptureConsumer(AsyncConsumer):
    async def capture_packets(self, event):
        cap = pyshark.LiveCapture(interface='eth0')
        packets = []

        async for packet in cap.sniff_continuously():
            packets.append(packet)
            # Here you can process or handle the packet
