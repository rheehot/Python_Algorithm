import sys

calendar = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
m,d = map(int,sys.stdin.readline().split())
total = 0
total += d
for i in range(m-1):
    total += calendar[i]
print(day[total%7])