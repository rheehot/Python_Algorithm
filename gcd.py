def gcd(a,b):
    return ( a if b == 0 else gcd(b,a%b) )

def gcd2(a,b):
    return gcd(b,a%b) if a%b else b

print(gcd(3,18))

print(gcd2(3,18))