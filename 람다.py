li = [9,2,4,3,10]
def A(a,b):
    return int(a)+int(b[0])

# lambda 인자 : 표현식( 이 자체가 리턴 )
print(map(lambda x: x%2==1, li))
print(list(map(lambda x: x%2==1, li)))
check_li = list(map(lambda x: x**2, li))
print(check_li)
print(A(10,list(map(lambda x: x%2==1,li))))