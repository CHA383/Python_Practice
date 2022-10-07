# 3항 연산자는 참인 경우와 거짓인 경우 다른 값을 갖는 것으로,
from tkinter import Y
from tkinter import X

X if T else Y
# 는 T가 True 일때 x, False일 때 y의 값을 갖는다.

# < 예시 >
def sgn(x):
  return 1 if x > 0 else (0 if x == 0 else -1)
# 이 코드는 부호 함수를 구현한다.