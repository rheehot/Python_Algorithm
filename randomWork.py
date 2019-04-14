import turtle as t
import random

t.shape("turtle")
t.speed(0)

m_c = int(input())
for x in range(m_c):
    a = random.randint(1,360)
    t.setheading(a)
    t.forward(10)