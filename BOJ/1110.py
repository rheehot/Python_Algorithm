n = int(input())
copy_n = n
first = 0
second = 0
temp = 0
count = 0
while True:
    if count == 0:
        first = n // 10
        second = n % 10
    if count != 0 and first == (copy_n // 10) and second == (copy_n % 10):
        print(count)
        break
    else:
        count += 1
        temp = first+second%10
        first,second = second, temp