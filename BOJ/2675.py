import sys

n = int(sys.stdin.readline())
for case in range(n):
    repeat, str_alpha = sys.stdin.readline().split()
    for i in range(len(str_alpha)):
        for j in range(int(repeat)):
            print(str_alpha[i],end='')
    print()