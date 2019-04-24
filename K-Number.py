def solution(array, commands):
    answer = []
    return_a = []
    for i in commands:
        print(i)
        print("처음 : ", i[0], "끝",i[1])
        for j in range(i[0]-1,i[1]):
            answer.append(array[j])
        answer.sort()
        print("A:",answer)
        return_a.append(answer[i[2]-1])
        answer = []
    return return_a

print("return : ",solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))