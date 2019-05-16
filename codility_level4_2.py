"""
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
"""def solution(A):
    A = list(set(A))
    A.sort()
    min_a = min(A)
    for i in range(len(A)):
        if A[i] == min_a:
            min_a += 1
        else:
            if A[i] < 0:
                return 1
            else:
                return min_a
    return min_a
"""
"""def solution(A):
    A = list(set(A))
    A.sort()
    min_a = min(A)
    max_a = max(A)
    len_a = len(A)
    if max_a == min_a + len_a + 1:
        return len_a + 1
    for i in range(len(A)-1):
        if A[i]+1 != A[i+1]:
            if A[i]+1 <= 0:
                return 1
            else:
                return A[i]+1
    return A[-1] + 1 
"""
# step 1. 중복값 제거
# step 2. 정렬
# step 3. 시작값이 없는 경우 양수든 음수든 결과는 1이기 때문에 1 출력
# step 4. 반복을 하면서 그 다음 값과 1 차이가 없을 때 원래 있어야 할 값을 리턴, 음수일 경우네는 어쨌든 양수 까지 넘어가야하니까 PASS
# step 5. 마지막으로 음수로 끝난 경우에 그냥 1 출력하고 아닌 경우에는 배열의 마지막 값에서 1을 더한 값을 출력
def solution(A):
    A = list(set(A))
    A.sort()
    if 1 not in A:
        return 1
    for i in range(len(A)-1):
        if A[i] + 1 != A[i+1]:
            if A[i]+1 <= 0:
                pass
            else:
                return A[i] + 1
    if A[-1] + 1 <=0:
        return 1
    else:
        return A[-1] + 1

print(solution([0,2,3,4,5,6,7,3,3,2,6,5,5]))
print(solution([-1,-2,0,1,2,3]))
print(solution( [1, 3, 6, 4, 1, 2]))