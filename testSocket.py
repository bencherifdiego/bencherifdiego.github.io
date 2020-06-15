import asyncio
import websockets
import time

msg = "global"

@asyncio.coroutine
def test(websocket, path):
    message = yield from websocket.recv()
    print(message)
    global msg
    msg = message

@asyncio.coroutine
async def test2(websocket, path):
    while True:
        global msg
        x = msg.split('|')
        for i in x:
            await websocket.send(i)
            await asyncio.sleep(0.01)
        

start_server = websockets.serve(test, "127.0.0.1", 1235)
start_server2 = websockets.serve(test2, "127.0.0.1", 1236)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(start_server2)
asyncio.get_event_loop().run_forever()