# 93.3점/100점 ... 하
import math
def solution(n,stations, w):
    answer = 0 ; start = 0
    count_list =[]
    for i in stations:
        i-=1
        count_list.append(i-w-start if i-w > 0 else 0)
        start = i+w+1 if i+w+1 < n-1 else n-1
    if start != n-1:
        count_list.append(n-1-start)
    for count in count_list:   
        answer += math.ceil(count/(2*w+1))
    return answer

# 테스트는 일부만 통과하고 효율성에서는 통과되는 소스코드
"""import math
def solution(n,stations, w):
    answer = 0 ; start = 0
    count_list =[]
    for i in stations:
        count_list.append(i-w-start if i-w >= 0 else 0)
        start = i+w if i+w < n else n
    if start != n:
        count_list.append(n-start)
    for count in count_list:
        answer += math.ceil(count/(2*w+1))
    return answer
"""
# 테스트는 다 통과하지만 효율성 면에서 문제가 되는 소스코드
"""import math
def solution(n, stations, w):
    answer = 0
    n_l = list()
    for i in range(n):
        n_l.append(0)
    for i in stations:
        i -= 1
        for j in range(i-w if i-w > 0 else 0,i+w+1 if i+w < n else n):
            n_l[j] += 1
    check_list = []
    count = 0
    for i in n_l:
        if i == 0:
            count += 1
        else:
            if count != 0:
                answer += math.ceil(count/(2*w+1))
            count = 0
    if count != 0:
                answer += math.ceil(count/(2*w+1))
    return answer"""

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))