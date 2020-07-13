#AMBIKESH JHA

import fbchat
from fbchat import Client
from getpass import getpass
import sys

#Logging Details For Facebook
print("Logging Details for Facebook...")
username = str(input("Username: "))
password = getpass()

#Login To Facebook
client = fbchat.Client(username,password)

#Details For Whom to Send Message and Number of Times To Send
name = str(input("Whom to send message: "))
msg = str(input("Type Message: "))
times = int(input("How Many Times To Send The Message: "))

#Exit If times exceeds 50
if times > 50:
    print("Number of times to send message exceeds 50.")
    sys.exit()

#Search For Users With Name As Key
friends = client.searchForUsers(name)

#Pick The User
friend = friends[0]

#Send the message
for i in range(times):
    sent = client.send(fbchat.models.Message(msg),friend.uid)
    print(i+1)
print("Message sent {} times successfully.".format(times))