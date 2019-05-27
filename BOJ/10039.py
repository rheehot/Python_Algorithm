import sys

avg_list = list()
for i in range(5):
    temp = int(sys.stdin.readline())
    avg_list.append(temp if temp >= 40 else 40)
print(sum(avg_list)//5)
