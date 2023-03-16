l = int(input("Enter length of list: "))
l1 = []
for x in range (l):
    l1.append(input("Enter element %d: " % (x+1)))
nl = []
for x in l1:
    if x not in nl:
        nl.append(x)

print("List after removing duplicates:", nl)
    