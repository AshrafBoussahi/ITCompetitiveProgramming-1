strings = ["AYOUB", "IS", "!BEST", "ITC", "BNADM"]

bigSize = len(strings[0])
for i in range(1, len(strings)):
    if len(strings[i]) > bigSize:
        bigSize = len(strings[i])

for i in range(bigSize + 4):
    print("*", end = '')

print()
for i in range(0, len(strings)):
    print("* ", end='')
    print(strings[i], end='')
    spaces = (bigSize +2) - len(strings[i]) - 1
    for j in range(spaces):
        print(' ', end='')
    print("*")

for i in range(bigSize + 4):
    print("*", end = '')


