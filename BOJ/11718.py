import sys

for i in range(100):
    temp = sys.stdin.readline()
    if temp == "\n":
        break
    else:
        print(temp[:-1])
    