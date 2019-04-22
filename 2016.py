def solution(a, b):
    month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    day=['SUN','MON','TUE','WED','THU','FRI','SAT']
    total_day = 0
    for i in range(0,a):
        total_day += month[i]
    total_day += b
    result = total_day % 7
    result = ( result + 5 ) % 7    
    return day[result]
month_l = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(1,14):
    for j in range(1,month_l[i-1]):
        print(solution(i,j),end='  ')
    print()