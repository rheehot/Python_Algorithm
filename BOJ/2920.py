import sys

str_list = list()
n_list = list(map(int,sys.stdin.readline().split()))
for i in range(len(n_list)-1):
    if n_list[i] < n_list[i+1]:
        str_list.append("ascending")
    else :
        str_list.append("descending")
str_list = list(set(str_list))
if len(str_list)> 1:
    print("mixed")
else:
    print(str_list[0])
