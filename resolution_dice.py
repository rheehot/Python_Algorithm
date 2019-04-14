def solution(A):
    count_list = []
    change_value_list = []
    for i in range(1,7):
        count_list.append(A.count(i))
    # print(count_list)
    for i in range(0,6):
        result = 0
        for j in range(0,6):
            if j == (7-i-2): #이부분이 마음에 걸리긴 하지만..
                result += 2 * count_list[j]
            elif i == j:
                pass
            else:
                result += count_list[j]
        change_value_list.append(result)
    return_value = min(change_value_list)
    return return_value

n_l = [1,6,3,5,2,6]
# print("len:",len(n_l))
print(solution(n_l))


