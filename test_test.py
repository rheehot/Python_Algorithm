def solution(s, n):
    result = []
    for i in range(len(s)):
        result.append(chr(ord(s[i])+n))
    result = "".join(result)
    return result
    
print(solution("AB",1))