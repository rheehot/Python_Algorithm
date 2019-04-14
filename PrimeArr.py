n = int(input())
a = []
i = 2
while i <= n:
    if n % i == 0:
        a.append(i)
        n /= i
    else:
        i += 1
print(a)