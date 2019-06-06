S = input() # 주어지는 값이 길이가 100을 넘지 않으며 알파벳 소분자로만 이루어져 있다.
alpabet_list = [-1]*26
# 'a'는 97
# print(ord('a')) 
check_list = list()
for i in range(len(S)):
    if S[i] not in check_list:
        check_list.append(S[i])
        alpabet_list[ord(S[i])-ord('a')] = i
for i in range(len(alpabet_list)):
    print(alpabet_list[i],end=' ')
 
# 나와야하는 출력 값
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 나온 출력 값 (리스트로 출력 시켰었음...)
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1