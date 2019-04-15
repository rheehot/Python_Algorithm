def biggest(n_l):
    n = len(n_l)
    big = 0
    for i in range(1,n):
        if n_l[big] < n_l[i]:
            big = i
    return n_l[big]

print(biggest([1,6,4,-1,12,3,8]))