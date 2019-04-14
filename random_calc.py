import random

a = random.randint(1,30)
b = random.randint(1,30)

print(a ," + ",b,"=")
x = int(input("결과는 ?"))

if a+b == x:
    print("정답입니다.")
else:
    print("틀렸습니다.")