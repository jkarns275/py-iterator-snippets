mylist = []

for value in range(16):
    mylist.append(value)

# prints: [0, 1, 2, 3, ..., 15] 
print(mylist)

# This accomplishes the same thing
mylist2 = []

myiter = iter(range(16)) 
while True:
    try:
        value = next(myiter)
    except StopIteration:
        break

    mylist2.append(value)

# prints: [0, 1, 2, 3, ..., 15] 
print(mylist2)

assert mylist == mylist2
