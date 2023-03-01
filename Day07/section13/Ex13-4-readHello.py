'''
r (read mode) : 읽기 전용 모드 / 파일 없으면 에러

경로
    절대경로 예) C:\pstudy\PythonProject\Day07\section13
    상대경로 예)
        . -> 현재 폴더 예) .//upload/hello2.txt
        .. -> 상위 폴더 예) ../../resources/hello.txt
'''
file = open('hello.txt', 'rt')
str = file.read()
print(str, end='')
file.close()

print()
with open('hello.txt', 'rt')as file:
    str = file.read
    str = file.read()
print(str, end='')
