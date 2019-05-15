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
def solution(A):
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

print(solution([1, 3, 6, 4, 1, 2,0]))
print(solution([-1,-2,0,1,2,3]))
print(solution( [1, 3, 6, 4, 1, 2]))