'''
죽음의 다이아몬드
'''
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):  # 오버라이딩 - 부모클래스 메소드 재정의
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B, C):
    pass   # 내부 동작 필요없고 빈껍데기만 필요할때 pass사용

x = D()
x.greeting()
print(D.mro())