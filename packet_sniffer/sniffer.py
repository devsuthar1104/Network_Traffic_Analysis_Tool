import asyncio
import pyshark

def capture_packets():
    cap = pyshark.LiveCapture(interface='eth0')
    packets = []

    # Define a coroutine function to capture packets
    async def capture():
        nonlocal packets
        async for packet in cap.sniff_continuously():
            # Process packet here, e.g., add it to a list
            packets.append(packet)

    # Run the event loop to capture packets
    loop = asyncio.get_event_loop()
    loop.run_until_complete(capture())

    # Return captured packets
    return packets
