def solution(dirs):
    a = { 'x' : 0, 'y' :0 }
    answer = 7
    point_list = list()
    m_list = list(dirs[::])
    for i in m_list:
        if i == 'U':
            a['y'] += 1
        elif i == 'D':
            a['y'] -= 1
        elif i == 'L':
            a['x'] -= 1
        elif i == 'R':
            a['x'] += 1
        else:
            break
        point_list.append({'x' : a['x'], 'y' : a['y']})
    print(point_list)
    return answer

solution("ULURRDLLU")