import random

n = random.randint(1,30)
bo = True
while bo:
    x = int(input("1~30 맞춰 보세요?"))
    if n == x:
        print("마자여")
        bo = False
    if n < x :
        print("너무커요")
    if n > x:
        print("작아요")
    