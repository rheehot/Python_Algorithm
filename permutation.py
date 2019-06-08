# https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations
# 원 작자의 소스 출처
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    # https://mingrammer.com/underscore-in-python/
    # 언더스코어(언더바)의 의미를 누구보다 잘 설명 해주심, 간단하게 설명하자면 그냥 무시하는거임, 0을 4개 호출
    def generate(chosen, used):
        # 2. 길이가 충족되면 출력 , 리스트에 저장하게 사용하려면 return 을 잘 활용하거나, 외부리스트에 append 시키면 될듯
        if len(chosen) == r:
            print(chosen)
            return
	
	# 3. 체크용으로 사용될 used 리스트에 값의 존재 유무로 추가한다.(재귀 또한 사용됨)
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                print('used : ',used)
                generate(chosen, used)
                used[i] = 0
                print('used : ',used)
                chosen.pop()
    generate([], used)

permutation('ABCD',3)

"""
1. 먼저 사용자가 원하는 arr 과 r 을 받는다. 그리고 arr 을 오름차순 정렬하는데 여기서는 큰 의미가 있지는 않고 단순히 출력을 이쁘게 하기 위해서이다. 
2. 그리고 used 변수를 만드는데, 이 변수는 i 번째 값을 썼는지 저장하는 데 쓰인다. 
3. 우리는 모든 순열을 하나씩 만들고 출력하는데 당연히 중복값은 저장되어서는 안 된다.
4. 실제 순열을 만들 generate 함수를 생성한다. 먼저 chosen 변수는 순열의 원소를 저장되는 변수인데 이 배열에 값을 하나씩 추가하다가 그 개수가 r 이 되는 순간 하나의 순열이 만들어진 것이므로 출력 후 종료한다.
5. 모든 순열은 arr 의 0부터 i-1 번째 값으로 시작하기에 for 문으로 다 만들어야 한다. 
6. 그리고 chosen 에 값 추가 후, used 에 해당 변수를 사용했다고 체크한다. 그 다음 다시 generate 를 반복한다. 하나가 만들어진 후에는 그 값을 uncheck해줘야 한다.
"""