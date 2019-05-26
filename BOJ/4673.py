check_list = [True] * 201
def check_value(c_v):
    temp = c_v
    for i in range(len(str(c_v))):
        temp += int(str(c_v)[i])
    check_list[temp-1] = False
    n = temp
    return check_value(n)

n = 1
while n < 100:
    if check_list[n-1] == True:
        check_value(n)
for i in range(1,101):
    if check_list[i] ==  True:
        print(i)

# 이 문제를 풀기위해서 생성자를 리스트에 추가하는 방법과 리스트에서 거르는 방법 두가지가 있을것으로 생각됨..
# 발표로 인해 추후에 풀 예정