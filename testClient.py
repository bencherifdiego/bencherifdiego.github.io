import asyncio
import websockets
import json
import base64
from PIL import Image
import time

@asyncio.coroutine
def test():
    websocket = yield from websockets.connect('ws://127.0.0.1:1235/')

    with open('view1.png', "rb") as imageFile1:
        img = str(base64.b64encode(imageFile1.read()).decode())

    conLines = open('console.txt', 'r').readlines()
    con = ''
    for line in conLines:
        con = con + line + '/'

    with open('data.txt') as json_file:
        data = json.load(json_file)
        m = '0 ' + data['lat'] + '|' + '1 ' + data['long'] + '|' + '2 ' + data['alt'] + '|' + '8 ' + con + '|' + '9 ' + img
        yield from websocket.send(m)

    time.sleep(0.01)

while True:
    asyncio.get_event_loop().run_until_complete(test())