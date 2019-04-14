import random

throw_count = 10000000
r_l = [0,0,0,0,0,0]
for i in range(throw_count):
    r_l[random.randint(1,6)-1] += 1
print(r_l)