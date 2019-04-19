def decTobin(num):
    return_n = ''
    while num > 0:
        if num % 2 == 0:
            return_n += '0'
        else:
            return_n += '1'
        num //= 2
    return return_n[::-1]
def main():
    num = int(input("정수를 입력하세요:"))
    print(decTobin(num))

main()