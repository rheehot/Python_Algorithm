# https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations
# 원 작자의 소스 출처
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    # https://mingrammer.com/underscore-in-python/
    # 언더스코어(언더바)의 의미를 누구보다 잘 설명 해주심, 간단하게 설명하자면 그냥 무시하는거임, 0을 4개 호출
    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

permutation('ABCD',2)