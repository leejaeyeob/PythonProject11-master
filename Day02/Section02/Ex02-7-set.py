"""
set

순서가 없다
인덱싱되지 않는 컬렉션
중복값 없다
"""

thisset = {"피카츄", "라이츄", "파이리"}
# 실행할 때 마다 순서가 변경 - 랜덤
print(thisset)

#항목 가져오기
for x in thisset:  # thisset 길이만큼 반복
    print(x)

# 값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("파카츄" in thisset)
print("라이츄" in thisset)

# 항목 추가하기
thisset.add("꼬부기")
print(thisset)

# 다른 set 항목 추가
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "뮤츠"}
thisset1.update(thisset2)
print(thisset1)

# 항목제거
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
# thisset.remove("피카츄")
# print(thisset)

# 항목제거 (에러가 나면 안되는 상황에 discard 사용)
thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)
thisset.discard("피카츄")
print(thisset)

# 항목제거
thisset.pop()
print(thisset)

# 비우기
thisset.clear()
print(thisset)
