def solution(n,road,K):
    answer = 0
    road.sort()
    check_list = list()
    for i in road:
        if i[0] > i[1]:
            i[0],i[1] = i[1],i[0]
    for i in range(len(road)):
        if road[i][0] == 1:
            check_list.append(road[i])
        else:
            for k in range(len(check_list)):
                if check_list[k][1] == road[i][0]:
                    if check_list[k][2] + road[i][2] <= K:
                        check_list.append([check_list[k][0],road[i][1],check_list[k][2]+road[i][2]])
    count = list()
    for i in range(len(check_list)):
        count.append(check_list[i][0])
        count.append(check_list[i][1])
    count = set(count)
    answer = len(count)            
    return answer

	
print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))