"""
a,b,c = 2
d,e,f = 3
g,h,i = 4 
j,k,l = 5
m,n,o = 6
p,q,r,s = 7
T,U,V = 8
w,x,y,z = 9
"""
import sys
# 여기에서 의미하는 2는 숫자 2를 의미하는 것
a = {
    "A" : 3,
    "B" : 3,
    "C" : 3,
    "D" : 4,
    "E" : 4,
    "F" : 4,
    "G" : 5,
    "H" : 5,
    "I" : 5,
    "J" : 6,
    "K" : 6,
    "L" : 6,
    "M" : 7,
    "N" : 7,
    "O" : 7,
    "P" : 8,
    "Q" : 8,
    "R" : 8,
    "S" : 8,
    "T" : 9,
    "U" : 9,
    "V" : 9,
    "W" : 10,
    "X" : 10,
    "Y" : 10,
    "Z" : 10
    }

test_str = sys.stdin.readline().rstrip()
total = 0
for i in range(len(test_str)):
    total += a[test_str[i]]
print(total)