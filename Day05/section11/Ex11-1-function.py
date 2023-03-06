'''
함수(fuction)
    하나의 특별한 목적의 작업을 수행하기 위해
    독립적으로 설계된 프로그램 코드의 집합.

def 함수이름(매개변수)
    코드 실행문
    return 반환값
'''

# welcome() 함수 정의(실행x)
def welcome():   # 매개변수 x 리턴 x
    print('Hello python')
    print('Nice to meet you')

welcome() # 함수 호출(실행)

# 매개변수 o, 리턴 x
def introduce(name, age):
    print('내 이름은 {}이고, 나이는 {}살 입니다.'.format(name, age))

introduce('이재엽', 23)

# 가변 매개변수 함수
def show(*args):
    for item in args:
        print(item)

show('python')
show('python', 'java', 'c')

# 반환(return) 값이 있는 함수
def address():   # 매개변수 x ,리턴 o
    str = '우편번호12345\n'
    str += '서울시 영등포구 여의도동'
    return str

result = address()
print(result)

# 매개변수 o 리턴 o
def plus(num1, num2):
    return num1 + num2

result = plus(5, 7)
print(result)
print(plus(2, 3))

area = 0
def rmove():
    global area
    area += 1

def lmove():
    global area
    area -= 1

rmove()
rmove()
rmove()
lmove()
lmove()

print('유닛이 오른쪽으로 {}칸 이동했습니다'.format(area))

