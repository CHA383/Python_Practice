# 파이썬 3.6 이상을 사용한다면, 문자열 formatting을 할 때 C style이나 str.format 메소드 말고 f-string 문법을 사용하자. 훨씬 간결한 코드를 작성할 수 있다.

name = "Paul"
age = 23
height = 175.324

# str.format 예시
introduction = "My name is {}. My age is {}. Mi height is {:.1f}".format

# f-string 예시
introduction = f"My name is {name}. My age is {age}. My height is {height:.1f}"

# 문자열을 합칠 때 join을 쓰자. range 함수와 str 함수를 같이 쓰면 매우 편해지는 경우가 있다.

''.join(str(x) for x in range(10))

# 슬라이스(slice) 문법은 리스트/문자열의 부분을 잘라내는 것 
# 이외에도 다양한 활용이 가능하다.

# 문자열 뒤집기
a = 'abc'
print(a[::-1]) # 출력: cba

# 리스트 복사
a = [1, 2, 3]
b = a[:]
print(b)      # 출력: [1, 2, 3]
print(a is b) # 출력: False

c = [[1, 2], [3, 4]]
d = c[:]
c[0] = [5, 6] # 리스트 자체는 복사되지만
c[1][0] = 7 # 리스트들의 원소들까지 복사되지는 않으므로 주의해서 사용하자.
print(c)  # 출력: [[5, 6], [7, 4]]
print(d)  # 출력: [[1, 2], [7, 4]]
print('%s, %s, %s' % (c is d, c[0] is d[0], c[1] is d[1])) # 출력: False, False, True

# 숫자, 문자, 튜플은 변경 불가능(immutable)하며, 리스트, 집합, 딕셔너리 변경 가능(mutable)하다. 이때 변경 가능한 자료형 다른 변수에 대입하여도 그 내용이 공유된다. 그 예로, 아래로 같은 코드가 있다고 하자.

a = (1, 2, 3)
b = a
b += (2, 1)
print(a)  # 출력: [1, 2, 3]
print(b)  # 출력: [1, 2, 3, 2, 1]

# 우리가 예상한 대로, 튜플 b만 변경되고, a는 변경되지 않는다. 위의 코드에서 튜플(immutable)을 리스트(mutable)로 바꾸어 보자.

a = (1, 2, 3)
b = a
b += (2, 1)
print(a)  # 출력: [1, 2, 3, 2, 1]
print(b)  # 출력: [1, 2, 3, 2, 1]

# 출력만 보면 b만 변경했음에도 a가 변한다는 사실을 알 수 있다. 이것은 모든 변겅 가능한 자료형에 적용되며, 심지어 리스트 안의 리스트 같은 것들까지도 공유가 된다. 그러니 원본을 변경하면 안 되는 경우에는 list(), set(), dict(), copy 모듈 등을 이용해서 객체를 복제하고 작업하자. 변경 불가능한 자료형은 원본을 변경할 수 없기 때문에 해당 사항이 없다. 특히 list나 dict 자체를 함수에 인자로 전달받을 때 내부에서 리스트를 변형하는 연산을 하면 함수 밖에서도 list나 dict가 변형되는 주의하도록 하자.