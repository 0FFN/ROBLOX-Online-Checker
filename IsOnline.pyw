import urllib.request
import json
from win10toast import ToastNotifier
from time import sleep as wait
notifier = ToastNotifier()
def IsOnlineNotify(user):
    notifier.show_toast("ROBLOX", user + ": => Online;", duration=5)
forever = 1

users = ["2829483765", "1910223575"] #-> Add the userid's here...

while forever == 1:
    for userid in users:
        reqinfo = json.load(urllib.request.urlopen('https://api.roblox.com/users/%s/onlinestatus/' % (userid)))
        IsOnline = reqinfo["IsOnline"]
        if IsOnline == True:
            reqinfo = json.load(urllib.request.urlopen('https://users.roblox.com/v1/users/%s' % (userid)))
            user = reqinfo["name"]
            IsOnlineNotify(user)
        wait(1)
    wait(25)
