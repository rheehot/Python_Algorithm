# O(n)
def sqrt_n(n):
    result = 0
    for i in range(1,n+1):
        result += i*i
    return result

# O(1)
def sqrt_n2(n):
    return n*(n+1)*(2*n+1) // 6


print(sqrt_n2(10))