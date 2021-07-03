
import requests
import time
from dhooks import Webhook


# Hypixel join pinger made by Duplexes#4335 for HaNicky#0244
# Put accounts in accounts.txt


#Config:

#Put discord webhook here:
hook = Webhook('https://discord.com/api/webhooks/860355674144112650/qiKRq6pPvp7e3Dkgjsi1tiFPJjmENRXWUKZBHw0Sxd0PQI39gcTP1PQh73giiWjmZ6ag')
#Put user ID to ping / role ID(ping user ID: <@USERIDHERE> ping role ID: <&ROLEIDHERE>):
notifcationPing = '<@323185194804969472>'
#Put Hypixel API key here: (Get key from /api in game)
hypixelAPIKey = '02948a82-9bc5-4f3d-af8a-0e423600284e'
#Time between checks if the users are online: (More accounts means higher time. If you get errors increase this.)
timeBetween = 60





my_file = open("accounts.txt", "r")
content = my_file.read()
content_list = content.split(",")
usersOnline = []
my_file.close()


while True:
    time.sleep(timeBetween)
    for x in content_list:
        responseMojang = requests.get('https://api.mojang.com/users/profiles/minecraft/' + x)
        if responseMojang.status_code == 200:
            jsonMojang = responseMojang.json()
            rawuuid = jsonMojang['id']
            uuidValid = True

        else:
            uuidValid = False
            rawuuid = 'false'
        responseHypixel = requests.get(f'https://api.hypixel.net/status?key={hypixelAPIKey}&uuid={rawuuid}')
        jsonHypixel = responseHypixel.json()
        print(jsonHypixel)
        userOnline = jsonHypixel['session']['online']
        time.sleep(3)

        if userOnline == True:
            if x not in usersOnline:
                usersOnline.append(x)
                print(f"{x} has joined Hypixel!")
                hook.send(f"{x} has joined Hypixel! {notifcationPing}")

        else:
            if x in usersOnline:
                usersOnline.remove(x)
                print(f"{x} has left Hypixel!")
                hook.send(f"{x} has left Hypixel! {notifcationPing}")



