'''
Ex02-9-mutalbe-immutable.py
mutalbe - 메모리 값을 변경 가능 객체
    리스트(list), 세트(set), 딕셔너리(dict)
'''
me = [1,2,3,]
print(id(me)) # 1967624158464
me.append(4)
print(id(me)) #list set dict는 주소값이 동일
'''
immutable - 메모리 값 변경 불가
    정수(int), 실수(float), 문자열(str), 튜플(tuple)
'''
me = 10
print(id(me))
me += 1 # me = me + 1
print(id(me)) #int float string tuple은 주소값이 변함