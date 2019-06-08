def combination(arr, r):
    # 1.
    arr = sorted(arr)

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])


combination('ABCDE', 2)
combination([1, 2, 3, 4, 5], 3)

"""
1. 입력은 순열 때와 같다. 
2. 배열도 마찬가지로 정렬한다.
3. 조합을 만드는 generate 함수를 만든다. 
4. 순열과 마찬가지로 chosen 에 저장된 아이템 개수가 r 개이면 조합이 하나 완성된 것이기 때문에 값을 출력하고 함수를 종료시킨다.
5. for 문을 돌리되, 시작을 chosen 에 저장된 마지막 값 다음으로 정한다. 이는 아까 순열함수와 대비되는 부분으로, 조합은 순열과 달리 순서를 고려하지 않고 뽑기 때문에, 가짓수를 제한해줘야 한다.
6. start 가 chosen 이 비어있을 경우 0이 되는 것도 참고한다. 빈값일 때는 그냥 0을 넣어야 한다.
"""