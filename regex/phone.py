import re
import os
os.chdir("/workspaces/py-low/regex/")

reg = r"(\d{3}-\d{3}-\d{4}|\d{10})"
file = open("input.txt.gi",'r').read()

print(re.findall(reg, file))