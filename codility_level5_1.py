# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    check_list = []
    for i in range(A,B):
        if i % K == 0:
            check_list.append(i)
    return len(check_list)

print(solution(6,11,2))