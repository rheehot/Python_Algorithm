import math
def solution(n,words):
    answer = []
    p_count = 1 % n
    check_words = list()
    for i in range(1,len(words)):
        p_count = n if (p_count + 1) % n == 0 else (p_count + 1) % n
        if words[i-1][-1] != words[i][0]:
            return [p_count,math.ceil((i+1)/n)]
        check_words.append(words[i-1])
        if words[i] in check_words:
            return [p_count,math.ceil((i+1)/n)]
    return [0,0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

"""import math
def solution(n, words):
    answer = []
    people = 0
    count = 0
    check_words = []
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0]:
            count = i+1
            people = 3 if (i+1) % n == 0 else (i+1) % n
        check_words.append(words[i-1])
        if words[i] in check_words:0

            count = i+1
            people = 3 if (i+1) % n == 0 else (i+1) % n
    check_words.append(words[-1])
    if count == 0:
        return [0,0]
    count = math.ceil(count/n)
    return [people,count]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
"""
# 사람이 n번호 , 차례는 그 사람의 순서
# 출력 값의 형태는 [번호, 차례]
# words 끝까지 무사히 통과하게 되면 0,0을 리턴

