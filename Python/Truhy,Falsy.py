# 일부 언어와 마찬가지로, 파이썬도 특정 값이나 객체에 참 또는 거짓의 
# 논리를 부여할 수 있다. 이는 논리 연산을 할 때 매우 유용하게 사용할 수 있다.

# 예를 들어 문자열이 유효한지 검사할 때
# str = ''
# if len(str) > 0: ~
# <------------------>
# str = ''
# if str: ~
# 와 같이 손쉽게 처리할 수 있다.

# 파이썬에서 기본적으로 특정 논리를 갖는 값은 다음과 같다.
# Truthy: True, 0이 아닌 수, 유효한 문자열(비지 않은 문자열), 유효한 리스트, 유효한 튜플
# Falsy: False, None, 0, 빈 문자열, 빈 튜플 등

# 그 외에도 자체적으로 선언한 객체에 bool 논리를 부여해 주려면 __bool__ 메소드를 사용하면 된다. 이 메소드가 없는 객체는 무조건 True로 취급된다.

class Value:
  def __init__(self):
    self.valid = False
  def __bool__(self):
    return self.valid
  def setValiduty(self, validty):
    self.valid = validty
var = Value()
print(bool(var)) # False
var.setValiduty(True)
print(bool(var)) # True