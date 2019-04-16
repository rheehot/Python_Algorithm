n_list = {1:1, 2:1}

def fibo(n):
    if n==0:
        return 0
    if n not in n_list:
        n_list[n] = fibo(n-1) + fibo(n-2)
    print(n_list)
    return n_list[n]
        
print(fibo(10))