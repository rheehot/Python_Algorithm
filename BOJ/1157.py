a = input()

count_list = [0]*26
for i in range(len(a)):
    if 65 <= ord(a[i]) and ord(a[i]) <= 90:
        count_list[ord(a[i])-65] += 1
    elif 97 <= ord(a[i]) and ord(a[i]) <= 122:
        count_list[ord(a[i])-97] += 1
    else:
        count_list[i]+=0
if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(chr(count_list.index(max(count_list))+65))