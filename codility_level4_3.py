def solution(N, A):
    # N이 배열 크기, A에서 값 확인후 모듈러 
    max_a = max(A)
    check_list = list()
    for i in range(N):
        check_list.append(0)
    for i in A:
        if i == max_a:
            max_c = max(check_list)
            for j in range(len(check_list)):
                check_list[j] = max_c
        else:
            check_list[(i%N-1)] += 1
    return check_list

solution(5, [3, 4, 4, 6, 1, 4, 4]) 
