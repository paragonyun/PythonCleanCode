"""인자들
- 위치 전용 인자 (Positional-only Parameter)
    - 키워드 사용이 필요 없어서 위치 인자를 사용하는 게 아니면 되도록 사용 x

- 키워드 전용 인자(keyword-only parameter)
    - *args가 그 것! *args로 시작을 알린다. *args 는 대충 그 사이의 위치 인자가 몇 개가 와도 상관 없다는 뜻!
    - 2개의 위치 인자만 쓰고싶으면 (position1, position2, *, kw1, kw2) 이런 시긍로 사용한다. 
    - def function(x, y, *args, kw1, kw2=0) 에서 kw1, kw2가 키워드 인자가 된다.
    - 함수에서 인자를 추가할 땐(wrapper) 키워드 인자를 사용하여 명확하게 하자.

"""
## 위치 전용 인자
def my_function(x, y, /):
    print(f"{x=} {y=}")


my_function(1, 2)  # x=1 y=2
my_function(2, 1)  # x=2 y=1
# my_function(x=1, y=2) ## TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'x, y'

## 키워드 전용 인자
def my_kw(x, y, *args, kw1, kw2=0):
    print(f"{x=} {y=} {kw1=} {kw2=}")


my_kw(
    1, 2, 3, 4, 5, 6, 7, kw1=100, kw2=1000
)  # x=1 y=2 kw1=100 kw2=1000 | *args를 쓰면 그 사이에 몇개가 와도 상관 없다.


def my_kw2(x, y, *, kw1=100, kw2=100000):
    print(print(f"{x=} {y=} {kw1=} {kw2=}"))


# my_kw2(1,2,3,4,5) ## TypeError: my_kw2() takes 2 positional arguments but 5 were given
