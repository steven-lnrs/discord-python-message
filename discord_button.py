
import requests
import time
import os
os.system('cls')
time.sleep(3)
webhookurl = input('what webhook would you like to use?\n')
time.sleep(1)
bot_name = input("what do you want to name the bot?\n")
time.sleep(1)
message = input("what would you like to send to the discord?\n")
time.sleep(1)
#how to send it
data = {
    "content" : message,

    "username" : bot_name
}

result = requests.post(webhookurl, json = data)
#check for error (shouldn't be any unless the discord webhook is invalid)
try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("sent".format(result.status_code))
