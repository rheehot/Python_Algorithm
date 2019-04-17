"""
    def solution(participant, completion):
        answer = ''
        for i in completion:
            participant.remove(i)
        answer = participant[0]
        return answer

    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
"""

"""
def solution(participant, completion):
    count_list = dict()
    for i in participant:
        count_list[i] = participant.count(i)
    for i in completion:
        count_list[i] -= 1
    for i in count_list.keys():
        if count_list[i] == 1:
            return i
"""
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))