
import requests
import time
from dhooks import Webhook
import yaml


# Hypixel join pinger made by Duplexes#4335 for HaNicky#0244
# Put accounts in accounts.txt



with open('config.yml', 'r') as f:
    config = yaml.load(f)
content_list = config['accounts']
usersOnline = []

hook = Webhook(config['discord']['webhookURL'])
notifcationPing = (config['discord']['mention'])
hookName = (config['discord']['webhookName'])
hookImageName = (config['discord']['webhookImageName'])
hypixelAPIKey = (config['hypixel']['APIKey'])
timeBetween = (config['hypixel']['alertTime'])

with open(hookImageName, 'rb') as f:
    img = f.read()  # bytes

hook.modify(name=hookName, avatar=img)

print("""
    __  __            _           ______  _            
   / / / /_  ______  (_)  _____  / / __ \(_)___  ____ _
  / /_/ / / / / __ \/ / |/_/ _ \/ / /_/ / / __ \/ __ `/
 / __  / /_/ / /_/ / />  </  __/ / ____/ / / / / /_/ / 
/_/ /_/\__, / .___/_/_/|_|\___/_/_/   /_/_/ /_/\__, /  
      /____/_/                                /____/   
      
      Made by Duplexes! Don't skid and sell! 
      
      Check my other projects out here: https://discord.gg/m2ww79zA6B   
""")

input("Press any key to start!")
print("Following names are being checked: ")
print(*content_list, sep = ", ")

while True:
    time.sleep(timeBetween)
    for x in content_list:
        try:
            responseMojang = requests.get('https://api.mojang.com/users/profiles/minecraft/' + x)
            jsonMojang = responseMojang.json()
            rawuuid = jsonMojang['id']
            responseHypixel = requests.get(f'https://api.hypixel.net/status?key={hypixelAPIKey}&uuid={rawuuid}')
            jsonHypixel = responseHypixel.json()
            userOnline = jsonHypixel['session']['online']
            time.sleep(10)
        except:
            print(f"[+] Ran into a error while checking status for {x}")
            continue

        if userOnline == True:
            if x not in usersOnline:
                usersOnline.append(x)
                print(f"[+] {x} has joined Hypixel!")
                hook.send(f"{x} has joined Hypixel! {notifcationPing}")

        else:
            if x in usersOnline:
                usersOnline.remove(x)
                print(f"[+] {x} has left Hypixel!")
                hook.send(f"{x} has left Hypixel! {notifcationPing}")



