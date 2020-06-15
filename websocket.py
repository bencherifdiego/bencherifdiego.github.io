import asyncio
import datetime
import random
import websockets
import cv2
import base64

async def time(websocket, path):

    with open('test.jpg', "rb") as imageFile1:
        img1 = '2 ' + str(base64.b64encode(imageFile1.read()).decode())

    with open('download.jpg', "rb") as imageFile2:
        img2 = '2 ' + str(base64.b64encode(imageFile2.read()).decode())

    test = True

    while True:
        now = '0 ' + datetime.datetime.utcnow().isoformat()
        temp = '1 ' + str(random.randrange(0, 10))
        await websocket.send(now)
        await websocket.send(temp)
        if test == True:
            await websocket.send(img1)
            test = False
            print("img1")
        elif test == False:
            await websocket.send(img2)
            test = True
            print("img2")
        await asyncio.sleep(2.5)

start_server = websockets.serve(time, "127.0.0.1", 1235)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()