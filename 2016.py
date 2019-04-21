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

print(solution(5,24))