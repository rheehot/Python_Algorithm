def solution(dirs):
    a = { 'x' : 0, 'y' :0 }
    answer = 0
    append_ok = True
    point_list = list()
    m_list = list(dirs[::])
    for i in m_list:
        if i == 'U':
            if a['y'] >= 5:
                append_ok = False
            else:
                a['y'] += 1
        elif i == 'D':
            if a['y'] <= -5:
                append_ok = False
            else:
                a['y'] -= 1
        elif i == 'L':
            if a['x'] <= -5:
                append_ok = False
            else:
                a['x'] -= 1
        elif i == 'R':
            if a['x'] >= 5:
                append_ok = False
            else:
                a['x'] += 1
        else:
            break
        if append_ok:
            point_list.append({'x' : a['x'], 'y' : a['y']})
        append_ok = True
    print(point_list)
    check_list = list()
    check_in = True
    for i in point_list:
        if i in check_list:
            if check_list.count(i) < 2 and check_in == True:
                check_list.append(i)
                answer += 1
                check_in = False
        else:
            check_list.append(i)
            answer += 1
            check_in =True
    print(check_list)
    return answer

print(solution("ULURRDLLU"))