'''
time 모듈
    시간 처리에 관련된 time 모듈
'''
import time
# 1970년 1월 1일 0시 0분 0초부터 현재까지 경과 시간을 반환
# 마이크로초
print(time.time())


# ctime() 함수 - 인수로 전달된 time 시간 형식을 갖춰 반환
print(time.ctime(time.time()))

# 인수로 전달된 날짜와 지시자를 이용하여 형식을 갖춘
# 날짜 데이터를 문자열로 전환
print(time.strftime('%y-%m-%d %H:%M:%S'))

# 만약 인코딩 문제 발생시 아래와 같이 사용하면됩니다.
print(
    time.strftime(
        '%y년 %m월 %d일'
        .encode('unicode-escape')
        .decode()
    ).encode().decode('unicode-escape')
)

time.sleep(1)

sec = 1
while True:
    print(sec, "초")
    if sec == 10:
        break
    time.sleep(1)
    sec += 1
