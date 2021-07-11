
import requests
import time
from dhooks import Webhook


# Hypixel join pinger made by Duplexes#4335 for HaNicky#0244
# Put accounts in accounts.txt


#Config:

#Put discord webhook here:
#hook = Webhook('')
#Put user ID to ping / role ID(ping user ID: <@USERIDHERE> ping role ID: <&ROLEIDHERE>):
notifcationPing = '<@>'
#Put Hypixel API key here: (Get key from /api in game)
hypixelAPIKey = ''
#Time between checks if the users are online: (More accounts means higher time. If you get errors increase this.)
timeBetween = 120





my_file = open("accounts.txt", "r")
content = my_file.read()
content_list = content.split(",")
usersOnline = []
my_file.close()

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



