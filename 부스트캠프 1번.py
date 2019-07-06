def solution(arr):
    count_arr = []
    arr.sort() # sort 해줄 필요가 있었나?
    set_arr = set(arr)
    for i in set_arr:
        if arr.count(i) == 1:
            pass
        else:
            count_arr.append(arr.count(i))
    if len(count_arr)<1:
        return [-1]
    else:
        return count_arr
    

print(solution([1,2,3,3,3,4,4]))
print(solution([3,2,4,4,2,5,2,5,5]))
print(solution([3,5,7,9,1]))