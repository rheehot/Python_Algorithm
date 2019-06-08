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