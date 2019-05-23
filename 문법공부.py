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

# 바로 실행 가능한 람다 식, 함수형 실행
(lambda x: x%2==1)(10)
print((lambda x: x if x%2==0 else 0)(10))

# 람다를 변수에 담을 수 있다.
dd = lambda x: x if x%2==0 else 0
print(dd(10))
# 람다를 쓰는 이유
# 간단하여, 줄을 줄일수있다. 

# 딕셔너리는 JSON 형태와 같으니 잘 쓸수있도록 공부해두기
dic = {'test':0,'name':0}
print(dic['test'])
print(dic.keys())

# 컴프리핸션
# 조금더 편리하게, 파이썬스럽게 코딩하는 법
a = [i for i in range(10)]
print(a)