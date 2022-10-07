# python의 조건문에서는 if, else 그리고 else if를 축약한 elif가 쓰인다.
# 예를 들어 부호 함수는 다음과 같이 쓸 수 있다.

def sgn(x):
  if x > 0:
    return 1
  elif x == 0:
    return 0
  else:
    return -1
    
# 사실 이 경우는 다음과 같이 써도 제대로 동작한다.
# 조건문 로직은 가독성과 퍼포먼스를 고려해서 적절히 설계할 필요가 있다.

def sgn(x):
  if x > 0:
    return 1
  if x == 0:
    return 0
  return -1
  
  # 다음은 변수 a의 대소 관계를 비교하는 코드이다.
  
  a = 50
  if a < 100:
    print(1)
  elif a > 90:
    print(2)
  else:
    print(3)
    