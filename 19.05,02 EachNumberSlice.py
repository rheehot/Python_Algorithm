def solution(numbers):
    answer = ''
    temp = list(numbers[::])
    r_temp = []
    for i in range(len(temp)):
        r_temp.append(list(str(temp[i])[::]))
    print(r_temp)
    return answer

solution([6,10,2])
