from time import time

def F_N(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

def U_F_N(n):
    return ((n * (n + 1))//2)

start_1 = time()
print(F_N(int(100000000)))
end_1 = time()
print(end_1 - start_1)
start_2 = time()
print(U_F_N(int(100000000)))
end_2 = time()
print(end_2-start_2)