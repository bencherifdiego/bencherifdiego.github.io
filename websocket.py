import asyncio
import datetime
import random
import websockets
import cv2

import pickle

async def time(websocket, path):
    #img = cv2.imread('shirt-1516073725-07c95537f06b1a9e6ec0100d7f70bef1.jpg')
    #data = pickle.dumps(img, 0)
    #size = len(data)
    #await websocket.send(data)
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 1234)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()