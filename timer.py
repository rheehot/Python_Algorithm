import time

print('시간 측정 합니다.')
start = time.time()
input("엔터누르면 엔터누를 시간까지 얼마인지 계산해줍니다.")
end = time.time()

result = end - start
print("걸린시간 : ",result)