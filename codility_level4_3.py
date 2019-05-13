# 맥스값이 얼마인지 미리 계산
# check_index로 가장 큰 값의 위치를 알아내기 위해서 값이 증가했을때 check_list에서 그 위치에 해당하는 값의 인덱스로 변경
# 계산하는 과정을 줄여보자..
def solution(N,A):
    check_index = 0
    max_v = max(A)
    check_list = [0] * N
    a_len = len(A)
    temp = 0
    for i in range(a_len):
        temp = A[i]%N-1
        if A[i]==max_v:
            if A[i] == 0:
                check_list = [check_list[check_index]]*N
            elif i == 0 :
                if a_len == 1:
                    check_list[temp] += 1
                else:
                    check_list = [check_list[check_index]] * N        
            else :
                check_list = [check_list[check_index]] * N
        else:
            check_list[temp] += 1
            if check_list[check_index] < check_list[temp]:
                check_index = temp
    return check_list

solution(5,[3,3,3,1,2,0])
solution(5,[3, 4, 4, 6, 1, 4, 4])
solution(1,[100000,99999,99999,99999])
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

