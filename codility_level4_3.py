def solution(N, A):
    mylist = [0] * N
    pre_max_flag = False
    max_val = 0
    for i in A:
        if (i == N+1) and pre_max_flag:
            continue
        if i <= N:
            mylist[i-1] += 1
            if mylist[i-1] > max_val:
                max_val = mylist[i-1]
            pre_max_flag = False
        else:
            mylist = [max_val] * N
            pre_max_flag = True
    return mylist

# 맥스값이 얼마인지 미리 계산
# check_index로 가장 큰 값의 위치를 알아내기 위해서 값이 증가했을때 check_list에서 그 위치에 해당하는 값의 인덱스로 변경
# 계산하는 과정을 줄여보자..
def solution(N,A):
    check_index = 0
    check_list = [0] * N
    a_len = len(A)
    flag = False
    for i in A:
        temp = i-1
        if (i == N+1) and flag:
            continue
        if i <= N:
            check_list[temp] += 1
            if check_list[temp] > check_list[check_index]:
                check_index = temp
            flag = False
        else:
            check_list = [check_list[check_index]] * N
            flag = True
    return check_list

solution(5,[3, 4, 4, 6, 1, 4, 4]) 
"""def solution(N, A):
    max_a = max(A)
    check_list = [0]*N
    a = len(A)
    for i in A:
        if i == max_a:
            if a == 1:
                check_list[(i%N-1)] += 1
            else:
                max_c = max(check_list)
                check_list = [max_c] * N
        else:
            check_list[(i%N-1)] += 1
    return check_list
"""

# 효율성 o(N x M)

# MAX 값이 여러개일 경우 치환이 여러번 일어나기 때문에 값의 연장이 일어남
# -> MAX 값이 여러 개임을 체크하고 곱하기를 해준 후 연산을 한번에 끝내는 것은 어떨까
# 1
# max 인덱스 값 위치를 찾는다
# 리스트의 모든 값을 모듈러 취한다
# 카운팅한다.

