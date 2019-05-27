import sys

# rstrip() 함수는 오른쪽에서 발생하는 개행 문자를 제외 함수인것 같다
# 추가적으로 매개변수로 char형의 변수를 넣을 수 있는데 이는 아마 해당 문자를 제외하는거 같다
temp = sys.stdin.readline().rstrip()
print(ord(temp))

# 반대로 돌리는 함수는 chr 이다
# ord chr 을 기억해서 아스키코드에 대한 문제를 풀수있도록 하자
# chr(65) = 'A' , ord('A') = 65