# 이 파일은 깃허브에 정상적으로 올라가는지 확인하기 위해 작성하는 파일입니다
class test():
    # 생성자는 요렇게
    a = 0
    b = 0
    def __init__(self, int_a, int_b):
        self.a = int_a
        self.b = int_b
    
    def sum(self):
        return self.a + self.b

a = test(10,20)

print(a.sum())