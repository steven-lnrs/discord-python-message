#this repo is still in development/the creator is kinda lazy
print('made by unusually_calm#8486')
import requests
#Please place your webhook here
webhookurl = ''
bot_name = input("what do you want to name the bot?\n")

message = input("what would you like to send to the discord?\n")
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
#this repo is still in development/the creator is kinda lazy
#made by unusually_calm#8486
import requests
#Please place your webhook here
webhookurl = input('what webhook would you like to use?\n')
bot_name = input("what do you want to name the bot?\n")

message = input("what would you like to send to the discord?\n")
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
