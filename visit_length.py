def solution(dirs):
    move_list = list(dirs[::])
    pos_list = list()
    pos = {'x': 0,'y':0}
    count_list = list()
    pos_list.append({'x' : pos['x'],'y' : pos['y']})
    for i in move_list:
        if i =='U':
            if pos['y'] < 5:
                pos['y'] += 1
                pos_list.append({'x' : pos['x'],'y' : pos['y']})
        elif i == 'D':
            if pos['y'] > -5:
                pos['y'] -= 1
                pos_list.append({'x' : pos['x'],'y' : pos['y']})
        elif i == 'R':
            if pos['x'] < 5:
                pos['x'] += 1
                pos_list.append({'x' : pos['x'],'y' : pos['y']})
        elif i == 'L':
            if pos['x'] > -5:
                pos['x'] -= 1
                pos_list.append({'x' : pos['x'],'y' : pos['y']})
    check_list=list()
    for i in range(1,len(pos_list)):
        check_list.append(str(pos_list[i-1])+"->"+str(pos_list[i]))
        check_list.append(str(pos_list[i])+"->"+str(pos_list[i-1]))
    check_list = set(check_list)
    answer = len(check_list)//2
    return answer


solution("ULURRDLLU")
solution("LULLLLLLU")
solution("LLRRRLLRL")

"""def solution(dirs):
    n_list = []
    for i in range(11):
        temp = []
        for j in range(11):
            temp.append(0)
        n_list.append(temp)
    x_pos = 5
    y_pos = 5
    answer = 0
    m_list = list(dirs[::])
    for i in m_list:
        print(x_pos,y_pos)
        n_list[y_pos][x_pos] += 1
        if i == 'U':
            if y_pos <= 10:
                y_pos += 1
        if i == 'D':
            if y_pos > 0:
                y_pos -= 1
        if i == 'L':
            if x_pos > 0:
                x_pos -= 1
        if i == 'R':
            if x_pos < 10:
                x_pos += 1
    n_list[y_pos][x_pos] += 1
    for i in range(11):
        for j in range(11):
            if n_list[i][j] > 0:
                answer += 1
    for i in range(11):
        print(n_list[i])
    return answer 

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
"""
"""def solution(dirs):
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
    for i in point_list:
        check_list.append(i)
        answer += 1
    count_list = list()
    for i in range(len(check_list)):
        count_list.append(check_list.count(check_list[i]))
    print(check_list)
    print(count_list)
    return answer

print(solution("ULURRDLLU"))"""


"""position1=[0,0]
position2=[0,0]
pas=[]
def U():
    if position1[1]==5:
      return
    position2[1] = position2[1]+1
    a='%d%d=>%d%d'%(position1[0], position1[1], position2[0], position2[1])
    b='%d%d=>%d%d'%(position2[0], position2[1], position1[0], position1[1])
    pas.append(b)
    pas.append(a)
    position1[1] = position1[1]+1
def D():
    if position1[1]==-5:
      return
    position2[1] = position2[1]-1
    a='%d%d=>%d%d'%(position1[0], position1[1], position2[0], position2[1])
    b='%d%d=>%d%d'%(position2[0], position2[1], position1[0], position1[1])
    pas.append(b)
    pas.append(a)
    position1[1] = position1[1]-1
def R():
    if position1[0]==5:
      return
    position2[0] = position2[0]+1
    a='%d%d=>%d%d'%(position1[0], position1[1], position2[0], position2[1])
    b='%d%d=>%d%d'%(position2[0], position2[1], position1[0], position1[1])
    pas.append(b)
    pas.append(a)
    position1[0] = position1[0]+1
def L():
    if position1[0]==-5:
      return
    position2[0] = position2[0]-1
    a='%d%d=>%d%d'%(position1[0], position1[1], position2[0], position2[1])
    b='%d%d=>%d%d'%(position2[0], position2[1], position1[0], position1[1])
    pas.append(b)
    pas.append(a)
    position1[0] = position1[0]-1

def solution(dirs):
    for i in dirs:
        if i=='U':
            U()
        elif i=='D':
            D()
        elif i=='R':
            R()
        elif i=='L':
            L()
    c=set(pas)
    return int(len(c)/2)"""