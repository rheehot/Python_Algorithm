def solution(n):
    answer = ''
    a=counting(n)
    for i in range(a):
        if n % 3 == 0:
            result = 4
        else:
            result = n % 3
        if n % 3 == 0:
            n //= 3; n -= 1
        else:
            n //= 3
        answer = answer + str(result)
    return answer[::-1]


def counting(n):
    count = 1
    result = pow(3,count)
    while n > result:
        count += 1
        result += pow(3,count)
    return count

for i in range(0,14):
    print(solution(i))

#################
# 다른 해결 방법 #
#################
def sol(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

print("놀라운 방법",sol(3))