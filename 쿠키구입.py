"""과자를 바구니 단위로 파는 가게가 있습니다. 이 가게는 1번부터 N번까지 차례로 번호가 붙은 바구니 N개가 일렬로 나열해 놨습니다.

철수는 두 아들에게 줄 과자를 사려합니다. 첫째 아들에게는 l번 바구니부터 m번 바구니까지, 둘째 아들에게는 m+1번 바구니부터 r번 바구니까지를 주려합니다. 단, 두 아들이 받을 과자 수는 같아야 합니다(1 <= l <= m, m+1 <= r <= N). 즉, A[i] 를 i번 바구니에 들어있는 과자 수라고 했을 때, A[l]+..+A[m] = A[m+1]+..+A[r] 를 만족해야 합니다.

각 바구니 안에 들은 과자 수가 차례로 들은 배열 cookie가 주어질 때, 조건에 맞게 과자를 살 경우 한 명의 아들에게 줄 수 있는 가장 많은 과자 수를 return 하는 solution 함수를 완성해주세요. (단, 조건에 맞게 과자를 구매할 수 없다면 0을 return 합니다)

제한사항
cookie의 길이는 1 이상 2,000 이하입니다.
cookie의 각각의 원소는 1 이상 500 이하인 자연수입니다."""
def solution(cookie):
    answer = 0
    temp = 0 ; temp2 = 0
    left_list = list()
    right_list = list()
    temp_list = list()
    check_list = list()
    o_check_list = list()
    for i in range(len(cookie)):
        left_list.append(list(cookie[:i:]))
        right_list.append(list(cookie[i::]))
    for i in range(len(cookie)):
        for k in reversed(left_list[i]):
            temp += k
            check_list.append(temp)
        for l in right_list[i]:
            temp2 += l
            o_check_list.append(temp2)
        temp = 0 ; temp2 = 0
        for k in range(len(check_list)):
            if check_list in o_check_list:
                temp_list.append(check_list[k])
        for k in range(len(o_check_list)):
            if o_check_list in check_list:
                temp_list.append(o_check_list[k])
        answer += max(temp_list)
        check_list = list()
        o_check_list = list()
        temp_list = list()
    return answer

print(solution([1,1,2,3])) # return 3
print(solution([1,2,4,5])) # return 0 구할 수 없다면

# 3중 반복 
# 시작 반복 하나
# 안에 반복 반반 하나씩