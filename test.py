# 가위 바위 보 게임
# import random

# game = 0 ;win = 0 ; draw =0 ; lose = 0
# while True:
#     com = random.randint(1,3)
#     user = int(input("가위(1),바위(2),보(3)을 입력해주세요!:"))
#     if user > 3:
#         break
#     else:
#         if user == 1: # 가위
#             if com == 1: # 가위
#                 print("비겼습니다.")
#                 draw += 1
#             elif com == 2: # 바위
#                 print("컴퓨터가 이겼습니다.")
#                 lose += 1
#             else: # 보
#                 print("당신이 이겼습니다.")
#                 win += 1
#         elif user == 2: # 바위
#             if com == 1: # 가위
#                 print("당신이 이겼습니다.")
#                 win += 1
#             elif com == 2: # 바위
#                 print("비겼습니다.")
#                 draw += 1
#             else: # 보
#                 print("컴퓨터가 이겼습니다.")
#                 lose += 1
#         else: # 보
#             if com == 1: # 가위
#                 print("컴퓨터가 이겼습니다.")
#                 lose += 1
#             elif com == 2: # 바위
#                 print("당신이 이겼습니다.")
#                 win += 1
#             else: # 보
#                 print("비겼습니다.")
#                 draw += 1
#         game += 1
# print("전체 : ",game,"승리 : ",win,"무승부 : ",draw,"패배 :",lose)


# 사용자로 부터 숫자를 게속 입력받다가 에러
# stop = True
# a = list()
# while stop:
#     temp = input()
#     try:
#         temp = int(temp)
#         a.append(temp)
#     except ValueError:
#         stop = False
# print(sum(a))


# 연습문제 7
import random
a = list(random.randint(1,1000) for _ in range(100))
print(a)
print(max(a))
# 다른 방법
a.sort()
print(a)
print(a[-1])

# 연습문제 8
import random
# 아무 변수에 영향 없이 해당 명령을 range의 범위만큼(100번) 돌려라는 명령어
a = list(random.randint(1,1000) for _ in range(100))
# a리스트 출력
print(a)
# 합계
print(sum(a))
# 평균
print(sum(a)/len(a))