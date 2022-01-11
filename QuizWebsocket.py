import asyncio
from websockets import connect
import helper

config = helper.read_config()

class QuizWebsocket:
    async def __aenter__(self):
        wss = config['APPSettings']['WSSUrl']

        self._conn = connect(wss)
        self.websocket = await self._conn.__aenter__()        
        return self

    async def __aexit__(self, *args, **kwargs):
        await self._conn.__aexit__(*args, **kwargs)

    async def send(self):
        await self.websocket.send("prices")

    async def receive(self):
        return await self.websocket.recv()