import sys

n = int(sys.stdin.readline())
m = input() #sys.stdin.readline()사용 시, \n 까지 입력되어서
total = 0
for i in range(len(m)):
    total += int(m[i])
print(total)