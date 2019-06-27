# 연속되는 값 입력받게 하는 가변인수선언
def calc(*li):
    print(li)
    lenght = len(li)
    min_index = 0; max_index = 0; total = 0; avg=0
    for i in range(1,lenght):
        if li[min_index] > li[i]:
            min_index = i
    for i in range(1,lenght):
        if li[max_index] < li[i]:
            max_index = i
    for i in range(lenght):
        total += li[i]
    avg = total/lenght
    return li[min_index],li[max_index],avg

print(calc(1,2,3,4,5))