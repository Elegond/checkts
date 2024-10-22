import docker
import requests
import os
client = docker.from_env()
Headers = { "Content-Type": "application/json" }
chat_id = os.environ.get('chatid')
bot_key = os.environ.get('botkey')
container = client.containers.get('AMP_TeamSpeak301')

for line in container.logs(stream=True, tail=1):
    l= str(line.strip())
    if " connected" in l: 
        print(l)
        pload = {"chat_id": str(chat_id), "text": "TS3: "+str(l.split("'",2)[1])+" connected", "disable_notification": False}
        r = requests.post("https://api.telegram.org/"+str(bot_key)+"/sendMessage", json=pload, headers=Headers)
        print(r.content)
    if "disconnected" in l: 
        print(l)
        pload = {"chat_id": str(chat_id), "text": "TS3: "+str(l.split("'",2)[1])+" disconnected", "disable_notification": True}
        r = requests.post("https://api.telegram.org/"+str(bot_key)+"/sendMessage", json=pload, headers=Headers)
        print(r.content)

