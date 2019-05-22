li = [9,2,4,3,10]
def A(a,b):
    return a + sum(b)

# lambda 인자 : 표현식( 이 자체가 리턴 )
print(map(lambda x: x%2==1, li))
print(list(map(lambda x: x%2==1, li)))
check_li = list(map(lambda x: x**2, li))
print(check_li,li)
print(A(10,list(map(lambda x: x%2==1,li))))
print(li)
# 리스트에 직접적으로 관여하진 않는다.
# 아래의 결과는 22가 나와야함
print(A(10,map(lambda x: x if x%2==1 else 0,li)))
# 나옴


# 컴프리핸션
# 조금더 편리하게, 파이썬스럽게 코딩하는 법
a = [i for i in range(10)]
print(a)