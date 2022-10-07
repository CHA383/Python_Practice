# Python에서 람다 함수의 사용은 가독성을 해치므로 추천되지 않는다. (PEP 8)
# 다만, 람다 함수의 적절한 사용은 편의성을 높여주므로 
# 가독성을 해치지 않는 정도로 적절히 사용하는 것이 좋다.

# 예를 들어, map함수나 functools 모듈의 reduce 함수와 lambda 함수의 궁합이 좋다.
# map은 iterable한 자료형으로, 함수와 다은 iterable한 객체로 만든다.
arr = map(func, iter)
arr[i] == func(iter[i]) # True

# reduce는 이변함수와 iterable한 객체를 인자로 받는 함수이다.
# reduce의 작용은 대략적으로 다음과 같다.
def reduce(func, iter):
  x = iter[0]
  for i in iter[1:]:
    x = func(x, i)
  return

# 이를 lambda 함수와 함께 사용하면 다음과 같이 사용할 수 있다.
arr = list(map(lambda x: x**3, range(7)))

print(arr) # [0, 1, 8, 64, 125, 216]

import functools
total = functools.reduce(lambda x, y: x+y, [1, 3, 4])

print(total) # 1 + 3 + 4 = 8