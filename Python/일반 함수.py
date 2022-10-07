# Python의 함수 정의 키워드는 def이다. 예시를 보자

def multiply(a, b):
  return a * b

# 이 함수는 a, b 두 숫자를 받아서 돌려준다.
# 하지만 굳이 인자를 가져오지 않아도 global 이라는 명령어를 사용하여 함수 안에서도
# 전역변수 사용을 명시할 수 있다.

a = 3
b = 5
def multiply():
  global a, b
  return a * b

# Python에서 변수가 여럿인 함수를 짤 떄 사용할 수 있는 방법으로 asterisk(*)를 사용하는 것이 있다. 변수명 앞에 asterisk를 하나 붙이면, 입력받은 변수들의 튜플을 의미한다.

def function(*args):
  print(args)
  
function(1, 2, 3, 4) # (1, 2, 3, 4)를 출력한다.

# Asterisk를 2개 붙인 것은 키워드 변수를 의미한다. 이때, (키워드 - 값)의 딕셔너리 형태가 된다. 이때, 키워드는 str 이다.

def function(**kwargs):
  print(kwargs)

function(a = 1, b = 2) # {'a': 1, 'b': 2} 를 출력한다.

# 일반 변수, 키워드 변수, asterisk를 붙인 변수, double asterisk를 붙인 변수가 모두 있다면, 키워드 > 일반 > **변수 > *변수 순서로 인식된다.

def function(a, b = 0, *args, **kwargs):
  print("a =", a)
  print("b =", b)
  print("args = ", args)
  print("kwargs = ", kwargs)
  
function(1, 2, 3, b = 4, i = 5)

# 결과
a = 1
b = 4
args = (2, 3)
kwargs = {'i' : 5}