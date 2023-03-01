'''
모듈 사용법2
from 모듈명 import 함수
from 모듈명 import 함수1, 함수2
from 모듈명 import * #모듈 안에 있는 모든 함수를 사용할때 사용함
'''
from converter import Kilometer_to_miles

miles = Kilometer_to_miles(150)
print('150km={}miles'.format(miles))
