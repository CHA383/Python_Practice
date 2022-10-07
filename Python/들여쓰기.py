# Python 특유의 디자인 철학에 따라 Python은 분기문과 반복문 등을 사용할 때 들여쓰기를 행해야 한다. 보통 권장되는것은 4번 띄어쓰기이지만, Python 자체에서 자동 들여쓰기의 칸수를 결정할 수 있고 Tab을 권장되지 않으나 일부 텍스트 에디터에서 Tab의 스페이스 개수를 설정할 수 있기 때문에 큰 문제는 아니다. 2번이든 4번이든 한번 했으면 그걸로 계속 써야 한다. 그렇지 않으면 예외 오류가 발생한다.


# 틀린 문법
if True:
    print("Hello Wolrd") # 4칸 들여쓰기
for n in range(0, 10):
  print(n) # 2칸 들여쓰기
# 문법 오류

# 맞는 문법
if True:
  print("Hello Wolrd") # 2칸 들여쓰기
for n in range(0, 10):
  print(n) # 2칸 들여쓰기