import sys
n, k = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))
n_list.sort()
print(n_list[k-1])