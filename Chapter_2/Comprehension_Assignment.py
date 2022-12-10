"""
일반적으로 컴프리헨션을 사용하면 코드를 간결하고 가독성 높게 짤 수 있다.
그러나 복잡한 연산을 해야한다면 일반 for 문이 더 나을 수 있다.
단순한 연산은 컴프리헨션을 쓰자!

할당표현식
컴프리헨션과 비슷하게 코드를 간결하게 해주는 역할
그러나 간결한 코드 = 좋은 코드가 아니다. 좋은 코드는 다른 사람이 읽어도 이해하기 좋은 코드지, 
짧다고 무조건 좋은 건 아니다!
"""

import time

## 컴프리헨션 예시
def cal(x):
    return x**2


numbers = []
start = time.time()
for i in range(1000000):
    numbers.append(cal(i))  # list.append()를 너무 반복적으로 호출
print("단순 For문")
print(time.time() - start)

start = time.time()
numbers = [cal(i) for i in range(1000000)]
print("컴프리헨션")
print(time.time() - start)


## 할당 표현식 예시
for i in range(100):
    x = i % 10 == 0
    if i % 10 == 0:
        print(i, x)

for i in range(100):
    if x := i % 10 == 0:
        print(i, x)
