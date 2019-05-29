import sys
check_list = []
count = 0
is_add_ok = True
n = int(sys.stdin.readline())
for count in range(n):
    temp = sys.stdin.readline().rstrip()
    copy_temp = temp
    check_list = list(set(copy_temp))
    for i in range(len(temp)):
        check = temp[i]
        if check in check_list and temp[i-1] != check:
            is_add_ok = False
            break
        else:
            check_list.append(check)
        print(check,check_list,is_add_ok)
    if is_add_ok == True:   
        count += 1
    else:
        pass
    is_add_ok == True
    check_list = []
print(count)