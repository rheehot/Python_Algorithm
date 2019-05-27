import sys

n = int(sys.stdin.readline())
temp = 0
count = 0
for i in range(n):
    str_temp = sys.stdin.readline()
    for j in range(len(str_temp)):
        if str_temp[j] == 'O':
            count += 1
            temp += count
        else:
            count = 0
    print(temp)
    temp = 0
    count = 0
