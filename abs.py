# 일단 abs 의 문제점이 있는지 한번 보자
print(abs(5))
print(abs(-3))
print(abs(5.0))
print(abs(-3.0))
print("-----------")
# ..? 깔끔한데? 그래도 .. math를 이용해서 구현하겠다고 하니.. 
import math

def m_abs(a):
    if type(a) == float:
        b = a * a 
        return math.sqrt(b)
    elif type(a) == int:
        if a >= 0:
            return a
        else:
            return -a
    else:
        return "잘못된 값 입니다."

print(m_abs(5))
print(m_abs(-3))
print(m_abs(5.0))
print(m_abs(-3.0))
