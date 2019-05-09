import math
# n과 stations에 들어가는 값들은 배열에 해당하는 값이니까 -1 해주는 것을 간과하지말자.
def solution(n,stations, w):
    answer = 0
    check_point = 0
    count_list = list()
    for i in stations:
        i -= 1
        min_i = i-w if i-w>0 else 0
        max_i = i+w if i+w<n else n
        if min_i - check_point >0:
            print(min_i, check_point)
            count_list.append(min_i - check_point)
        check_point=max_i+1 # 안에서 비교할때는 그 다음 부터 진행을 해야하지만 마지막 비교값에서는 하나가 남을 수도 있기 때문에 -1을 한다
    check_point -= 1 # 마지막 비교값까지 가지 못하였기 때문에 마지막 비교값을 할 수 있게 해주어야 한다.
    if n-1-check_point >=0:
        count_list.append(n-1-check_point)
    print(count_list)
    for count in count_list:
        answer += math.ceil(count/(2*w+1))
    return answer
"""# 93.3점/100점 ... 하
import math
# n과 stations에 들어가는 값들은 배열에 해당하는 값이니까 -1 해주는 것을 간과하지말자.
def solution(n,stations, w):
    answer = 0
    check_point = 0
    count_list = list()
    for i in stations:
        i -= 1
        min_i = i-w if i-w>0 else 0
        max_i = i+w if i+w<n else n
        if min_i - check_point >0:
            print(min_i, check_point)
            count_list.append(min_i - check_point)
        check_point=max_i+1
    if n-1-check_point-1 >=0:
        count_list.append(n-1-check_point)
    print(count_list)
    for count in count_list:
        answer += math.ceil(count/(2*w+1))
    return answer"""
"""
import math
def solution(n,stations, w):
    answer = 0 ; start = 0
    count_list =[]
    for i in stations:
        i-=1
        count_list.append(i-w-start if i-w-start > 0 else 0)
        start = i+w if i+w < n-1 else n-1
    if start != n-1:
        count_list.append(n-1-start)
    print(start,count_list)
    for count in count_list:   
        answer += math.ceil(count/(2*w+1))
    return answer
"""
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

#print(solution(11, [4, 11], 1))
#print(solution(16, [9], 2))
#print(solution(5, [1,2,3], 1))
#print(solution(11, [1,2,5,8], 1))



"""def solution1(n, stations, w):
    count=0
    rng=w*2+1
    c=len(stations)
    p1 = stations[0]-1
    p2 = stations[c-1]+w
    while p1>0:
        p1-=rng
        count+=1
    while p2<n:
        p2+=rng
        count+=1
    if len(stations)!=1:
        for i in range(c-1):
            z=(stations[i+1]-w)-(stations[i]+w)
            if z<1:
                pass
            elif z%rng==0:
                count+=z//rng
            else:
                count+=int(z/rng)+1
    return count"""