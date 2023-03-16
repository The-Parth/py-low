import re

regex = r"^[456]((\d{15})|(\d{3}(-\d{4}){3}))$"

st = input()
result  = re.match(regex, st)
if result!=None:
    print("valid")
else:
    print("not valid")