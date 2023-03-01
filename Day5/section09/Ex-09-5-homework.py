'''
주말 숙제
Hint - len 함수 사용
[회원가입]
아이디를 입력하세요(3글자 이상) >>>
>3글자 이상 입력해주세요!

아이디를 입력하세요(3글자 이상) >>>

패스워드를 입력하세요(영문, 숫자 포함 8자 이상) >>>
>영문 숫자 포함 8자 이상 입력해 주세요!

패스워드 확인 한번 더 입력하세요 >>>
> 일치하지 않습니다! 다시 입력해 주세요!

패스워드를 입력하세요(영문, 숫자 포함 8자 이상) >>>

패스워드 확인 한번 더 입력하세요 >>>

화원가입 완료!


[로그인]

아이디를 입력하세요 >>>
>아아디가 일치하지 않습니다.

아이디를 입력하세요 >>>

패스워드를 입력하세요 >>>
>패스워드가 일치하지 않습니다.

패스워드를 입력하세요 >>>

로그인 성공!
000님 환영합니다!
'''

id = None
pwd = None

# 첫번째 아이디 입력
while True:
    id = input('아이디를 입력하세요 (3글자 이상 >>> ')
    if len(id) > 2:
        break
    print('>3글자 이상 입력해 주세요')

# 패스워드 입력
while True:
    pwd = input('패스워드를 입력해주세요(영문, 숫자 포함 8자이상) >>> ')
    isContainAlpha = False
    isContainNumberic = False
    if len(pwd) < 3:
        print(">영문 숫자 포함 8자 이상 이볅해주세요")
        continue

    for ch in pwd:
        if ch.isalpha():
            isContainAlpha = True
        elif ch.isContainNumberic = True

# 영문 포함 유효성 검사
if not isContainAlpha:
    print("영문, 숫자 포함 8자 이상 입력해주세요.")
    continue

# 숫자 포함 유효성 검사
if not isContainNumberic:
    print("영문, 숫자 포함 8자 이상 입력해주세요")

# 패스워드 확인 유효성 검사
pwdchk
if pwd != pwdchk



# 로그인 아이디
while True:
    loginid = input("아이디를 입력하세요 >>> ")
    if id == loginid:
        break
    print('>아이디가 일치하지 않습니다.')
# 로그인 패스워드
while True:
    loginpwd = input("패스워드를 입력하세요 >>> ")
    if id == loginpwd:
        break
    print('>패스워드가 일치하지 않습니다.')

print('로그인 성공')
print('{}님 환영합니다.'.format(id))
