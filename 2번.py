#-*- coding:utf-8 -*-
"""
올바른 괄호란 (())나 ()와 같이 올바르게 모두 닫힌 괄호를 의미합니다. )(나 ())() 와 같은 괄호는 올바르지 않은 괄호가 됩니다. 괄호 쌍의 개수 N이 주어질 때, N개의 괄호 쌍으로 만들 수 있는 모든 가능한 괄호 문자열을 배열형태로 반환하는 함수 solution을 완성해 주세요. 반환되는 문자열 배열은 오름차순으로 정렬되어 있어야 합니다.
< 제한사항 >
괄호 쌍의 개수 N : 1 ≤ N ≤ 12, N은 정수
"""
import itertools
stack = ["(",")"]

def solution(N):
    if N <1 or N > 13:
        return 
    answer = []
    for i in itertools.permutations(stack):
        if check(list(i)):
            answer.append(''.join(list(i)))
    return answer

def check(check_list):
    st = []
    for ck in check_list:
        if ck == "(":
            st.append(ck)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return True
"""
1개의 괄호쌍으로는 [ () ]
2개의 괄호쌍으로 [ (()), ()() ]의 2가지를 만들 수 있습니다.
3개의 괄호쌍으로 [ ((())), (()()), (())(), ()(()), ()()() ]의 5가지를 만들 수 있습니다.
4개의 괄호쌍이면 [(((()))),  ]
"""
print(solution(0))
