"""

이건 뭐가 틀린걸까, 출력값에 대해 조건을 맞추어 줘도 문제고.. 음.. 뭐지..

"""
import sys

n = int(sys.stdin.readline())
for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    total_avg = int(sum(temp[1:])/temp[0])
    count = 0
    check = temp[1:]
    for j in range(temp[0]):
        if check[j] > total_avg:
            count += 1
    print(str('%.3f' % round(count/temp[0]*100,3)) + '%')
# 강제로 붙이는게 아니였어... ㅠ