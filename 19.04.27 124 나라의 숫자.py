def solution(n):
    answer = ''
    print(counting(n))

def counting(n):
    count = 1
    result = pow(3,count)
    while n > result:
        count += 1
        result += pow(3,count)
    return count

print(solution(13))