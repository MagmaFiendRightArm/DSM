# ╔═╗╔═╗╔═╗╔═╗╦  ╦╔═╗╦╔╗╔╔═╗╔═╗╦ ╦
# ╚═╗║╣ ╚═╗║ ║║  ║╚═╗║║║║╠═╣║  ╠═╣
# ╚═╝╚═╝╚═╝╚═╝╩═╝╩╚═╝╩╝╚╝╩ ╩╚═╝╩ ╩
# ╔═════════════════════════════╗
# ║  Made by MagmaFiendRightArm ║
# ╚═════════════════════════════╝

import requests
import json
import websocket
import threading
import time

baseurl = "https://discord.com/api/v9"
usertoken = "discord token here"

headers = {
    "authorization": usertoken,
    "content-type": "application/json"
}

def sendheartbeat(ws):
    while True:
        ws.send(json.dumps({"op": 1, "d": None}))
        time.sleep(41.25)

def spoofnitrostatus(ws):
    payload = {
        "op": 3,
        "d": {
            "status": "online",  # change to "dnd", "idle", "invisible", "offline"
            "since": 0,  # time u started ur status, 0 = now
            "activities": [
                {
                    "type": 1,  # change to 0 (playing), 2 (listening), 3 (watching), 4 (custom status)
                    "url": "https://www.twitch.tv/discord",  # url if type is 1
                    "timestamps": {
                        "start": int(time.time() * 1000)  # start time of the activity
                    },
                    "state": "lmaoooooooooooooooo",  # custom status msg
                    "name": "Twitch",  # name of the activity (like game or app)
                    "details": "Rawdogging Sex",  # details bout the activity
                    "assets": {
                        "largeimage": "twitch:discord",  # big img key (from the app's rich presence assets)
                        "largetext": "Discord"  # text when u hover over the big img
                    }
                }
            ],
            "afk": False  # change to true if u wanna be afk (away from keyboard)
        }
    }
    ws.send(json.dumps(payload))

def onmessage(ws, message):
    data = json.loads(message)
    if data['op'] == 10:
        threading.Thread(target=sendheartbeat, args=(ws,)).start()
        spoofnitrostatus(ws)

def onerror(ws, error):
    print(f"Error: {error}")

def onclose(ws, closestatuscode, closemsg):
    print(f"WebSocket closed: {closestatuscode} - {closemsg}")

def onopen(ws):
    print("WebSocket connection opened")
    identifypayload = {
        "op": 2,
        "d": {
            "token": usertoken,
            "properties": {
                "$os": "windows",  # ur os (can be "windows", "macOS", etc.)
                "$browser": "chrome",  # browser (can be "chrome", "firefox", etc.)
                "$device": "pc"  # device type (can be "pc", "mobile", etc.)
            }
        }
    }
    ws.send(json.dumps(identifypayload))

def main():
    gatewayresponse = requests.get(f"{baseurl}/gateway")
    gatewayurl = gatewayresponse.json()['url']

    ws = websocket.WebSocketApp(f"{gatewayurl}/?v=9&encoding=json")
    
    ws.on_open = onopen
    ws.on_message = onmessage
    ws.on_error = onerror
    ws.on_close = onclose

    ws.run_forever()

if __name__ == "__main__":
    main()
