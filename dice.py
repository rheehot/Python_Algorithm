def solution(A):
    count_list = []
    result = 0
    if check(A):
        for i in range(1,7):
            count_list.append(A.count(i))
        count_list.sort()
        for i in range(len(count_list)):
            if count_list[i] != 0:
                result += 2*count_list[i]
                return result
    else:
        result
        for i in range(1,7):
            count_list.append(A.count(i))
        count_list.sort()
        for i in range(len(count_list)-1):
            if count_list[i] != 0:
                result += count_list[i]
        return result
    
    
def check(A):
    check_list = []
    for i in range(1,len(A)):
        if A[0] == A[i] or (7-A[0]) == A[i]:
            check_list.append(True)
        else:
            check_list.append(False)
    for i in range(len(check_list)):
        if check_list[i] != True:
            return False
    return True

print(solution([1,2,3,6]))

