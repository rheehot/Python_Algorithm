while True:
    # 끝 지점에 대한 예외처리를 통해 처리
    try:
        print(input())
    except EOFError:
        break