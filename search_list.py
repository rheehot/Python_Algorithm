def search_list(v,x):
    n = len(v)
    for i in range(0,n):
        if x == v[i]:
            return i
    return -1
v = [17,92,18,33,58,7,33,42]
print(search_list(v,18))
print(search_list(v,33))
print(search_list(v,900))