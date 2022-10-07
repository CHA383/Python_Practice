# 기본적으로 출력은 print(), 입력은 input()을 사용한다.
# input()은 기본적으로 str 형태로 값을 받으며, 특정 자료형 함수를 이용하면 다른 형으로 값을 받을 수 있다. 만약 그 형으로 값이 나오지 않으면 예외 오류가 일어난다.

print("Hello World!")
print("%d" %int)
print("%s" %str)

a = input("input")
b = int(input("input"))
c = float(input("input"))

# 입력에서 걸리는 시간을 줄이려면 sys 모듈의 stdin.readline()을 이용하면 좋다. 다만, 이 경우는 input과는 달리 입력받는 기능만을 할 수 있다.

import sys
a = sys.stdin.readline()
b = int(sys.stdin.readline()) 
c = float(sys.stdin.readline())
