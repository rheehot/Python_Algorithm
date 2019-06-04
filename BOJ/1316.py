import sys
n = int(sys.stdin.readline())
count = 0
for i in range(n):
    will_check_text = sys.stdin.readline().rstrip()
    will_check_text_length = len(will_check_text)
    temp = ""
    temp_list = list()
    for j in range(will_check_text_length):
        if temp != will_check_text[j] and will_check_text[j] not in temp_list:
            temp = will_check_text[j]
            temp_list.append(will_check_text[j])
        else:
            if temp == will_check_text[j]:
                pass
            else:
                count += 1
                break
print(n-count)