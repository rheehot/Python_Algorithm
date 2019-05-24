import sys

n = int(sys.stdin.readline())
for i in range(1,n+1):
    print("*"*(n-i+1))

"""

아래의 소스와 다른점을 알고싶다.. 위의 소스가 더 간결하고 좋긴함!!

"""
import sys

n = int(sys.stdin.readline())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end='')
    for j in range(n-i):
        print(" ",end='')
    print()