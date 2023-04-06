st = input("Enter your string: ")

dc = lc = 0

for ch in st:
    if ch.isdigit():
        dc += 1
    elif ch.isalpha():
        lc += 1

print("Digits: ",dc)
print("Letters: ",lc)