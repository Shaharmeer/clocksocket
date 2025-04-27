import asyncio
import datetime
from channels.generic.websocket import AsyncWebsocketConsumer

class ClockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            await self.send(now)
            await asyncio.sleep(2)

    async def disconnect(self, close_code):
        pass
