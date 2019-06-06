n = int(input())
for i in range(n):
    n_list = list(map(int,input().split()))
    total = 0
    for j in range(len(n_list)):
        if n_list[j] % 2 == 1:
            total += n_list[j]
    print("#",end='')
    print(i+1,end=' ')
    print(total)