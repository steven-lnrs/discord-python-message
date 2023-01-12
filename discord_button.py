#this repo is still in development/the creator is kinda lazy
#made by unusually_calm#8486
import requests
#Please place your webhook here
webhookurl = ''

message = input("what would you like to send to the discord?\n")
#how to send it
data = {
    "content" : message,

    "username" : "python test"
}

result = requests.post(webhookurl, json = data)
#check for error (shouldn't be any)
try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("sent".format(result.status_code))
