"""
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력 예
number	k	return
1924	2	94
1231234	3	3234
4177252841	4	775841
출처
"""
# if 문에서 남아있는 갯수가 널널하면, 앞의 값이 뒤엣 값 보다 작으면 앞에값 없에고 뒤에꺼 너으면 되지
# else 조건은 그대로 가고, 대신 min 으로 하게되면 자꾸 못들어가니께..
def solution(number, k):
    number = str(number)
    num_list = list(number[::])
    answer_temp = list()
    answer = ''
    for i in range(len(num_list)):
        if len(answer_temp) < len(num_list)-k:
            answer_temp.append(num_list[i])
        else:
            min_a = min(answer_temp)
            if min_a < num_list[i]:
                del answer_temp[answer_temp.index(min_a)]
                answer_temp.append(num_list[i])
    print(answer_temp)
    return answer

print(solution(1924,2)) #94
print(solution(1231234,3)) #3234
print(solution(4177252841,4)) #94
