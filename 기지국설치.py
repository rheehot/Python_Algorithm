import math
def solution(n, stations, w):
    answer = 0
    n_l = list()
    for i in range(n):
        n_l.append(0)
    for i in stations:
        i -= 1
        # 최고 범위값보다 항상 1 적게 범위를 설정하기 때문에 임의로 1을 더해줌
        # 삼항 연산자를 통해서 최소값 최대값 범위가 오게 되면, 최소값 혹은 최대값 범위까지 오게 설정
        for j in range(i-w if i-w > 0 else 0,i+w+1 if i+w < n else n):
            n_l[j] += 1
    check_list = []
    count = 0
    for i in n_l:
        if i == 0:
            count += 1
        else:
            if count != 0:
                check_list.append(count)
            count = 0
    check_list.append(count)
    print(n_l)
    print(check_list)
    for i in check_list:
        answer += math.ceil(i/(2*w+1))
    return answer

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))