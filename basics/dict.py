dict = {}
inp = input('Enter a word: ').upper()
for ch in inp:
    if ch in dict:
        dict[ch] += 1
    else:
        dict[ch] = 1
print(dict)
