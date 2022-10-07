#  C와 달리 파이썬은 변수를 선언할 때 따로 자료형을 지정하지 않는다.

# str() -float 형이나 int 형을 반환할 떄 사용한다. 제일 기본적으로 쓰인다.
# int() -정수형이다. float 형은 반올림한다.
# float() -실수형이다.
# complex() -복소수형이다. 허수는 i가 아니라 j로 표기한다.
# list()와 tuple()은 서로간 형 변환을 할 때 사용된다.

# 파이썬은 객체 지향 언어이고 원시 자료형이 없기 때문에 모든 값은 반드시 객체로 간주된다. 따라서 모든 데이터의 자료형은 그 데이터의 클래스이다.

class Value:
    pass
    
var = Value()
print(type(var)) # <class '__main__.Value'>
