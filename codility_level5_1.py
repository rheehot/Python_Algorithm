import math
def solution(A,B,K):
    if A==B:
        if A == 0:
            return 1
        elif A%K==0:
            return 1
        else:
            return 0
    else:
        if B % K == 0:
            return math.ceil((B+1-A)/K)
        else:
            if A % K == 0:
                return math.ceil((B+1-A)/K)
            else:
                if A < K:
                    return math.ceil((B+1-A)/K)
                else:
                    return math.ceil((B+1-A)/K)-1
# 아아아아 for 문으로 시도하면 정답은 확실하게 나오는데 속도가 나오질 않고 속도를 따지면 문제가 해결이 안되는 뫼비우스의 띠가 발생한다
# 아우ㅏㅇ뉠누이룬이ㅏㅜㄹㄴ;ㅁ