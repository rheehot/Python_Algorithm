def solution(N,A):
    check_v = 0
    max_v = max(A)
    check_list = [0]* N
    a_len = len(A)
    for i in range(a_len):
        if A[i]==max_v:
            if i == 0:
                check_list[A[i]%N-1] += 1
            else :
                check_list = [check_list[check_v]]*N
        else:
            check_list[A[i]%N-1] += 1
            if check_list[check_v] < check_list[A[i]%N-1]:
                check_v = A[i] % N - 1
    return check_list

# 맥스 값의 위치를 구했기 때문에 
# 체크 리스트의 맥스 값을 구하기 위해서 변수를 하나 선언을 하고
# 선언한 변수를 가지고 초기화 [max_!] * n을 시켜서 계산할 수 있도록 진행
#solution(5,[3,3,3,1,2,0])
solution(5,[3, 4, 4, 6, 1, 4, 4])
solution(10,[1,1,1,1,1,1,1,1,1,1])
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

