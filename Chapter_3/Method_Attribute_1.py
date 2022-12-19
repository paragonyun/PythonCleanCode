"""함수의 메서드와 인자
- Mutable을 쓰면 안 되는 이유
    - 파이썬의 함수가 인자를 호출할 땐 __defaults__에 있는 값을 가지고 온다.
    - 가변인자를 사용하게 되면 이 defaults에 있는 값이 바뀌기 때문에 기존의 초기화된 값을 사용할 수 없는 것! 아래의 코드 예시를 참고하자.

- 가변인자
    - 패킹 : 해당 인자를 해킹할 변수의 이름 앞에 *를 사용한다.
    - 언패킹 : 코드 예시 참고
    - 언패킹의 가장 좋은 예시는 반복이다. 일련의 요소를 차례대로 반복해야 할 때 언패킹을 하는 것이 좋다.
    - **은 아래와 같은 기능을 한다.
    ```
    function(**{"param_one":value_1}) = function(param_one=value_1)
    ```
"""

## 함수의 인자가 복사되는 방식
"""
함수에 값을 전달하면 그 값을 변수에 할당하고 나중에 사용
mutable 객체를 전달했는데 함수 안에서 값을 변경하면 파라미터의 내용이 변경되기도 함.
"""


def function(arg):
    arg += " in function"
    print(arg)


immutable = "hello"
function(immutable)  # hello는 변하지 않는 값이다.
mutable = list("hello")
function(mutable)  # 이때의 hello는 list로 변할 수 있는 값이 된다.

print(
    f"function 함수 이후의 값\nimmutable:hello->{immutable}\nmutable:{list('hello')}->{mutable}"
)


## 가변인자(패킹과 언패킹)
def f(one, two, three):
    print(one)
    print(two)
    print(three)


l = [1, 2, 3]
f(*l)  # 1 2 3

a, b, c = [1, 2, 3]
print(a, b, c)  # 1 2 3


def show(e, rest):
    print(f"요소 : {e}, 나머지 : {rest}")


e, *rest = [1, 2, 3, 4, 5]
show(e, rest)  #  요소 : 1, 나머지 : [2, 3, 4, 5]

*rest, e = [1, 2, 3, 4, 5]
show(e, rest)  # 요소 : 5, 나머지 : [1, 2, 3, 4]

e1, *rest, e2 = [1, 2, 3, 4, 5]
print(e1, rest, e2)  # 1 [2, 3, 4] 5

e1, e2, *rest = 1, 2
print(e1, e2, rest)  # 1 2 []

"""언패킹의 좋은 예시"""
from dataclasses import dataclass

USERS = [
    (i, f"first_name_{i}", f"last_name_{i}")
    for i in range(1_000)  # _는 언더바 없는 거랑 같은 수를 의미함. 그냥 숫자 읽기 편하게 만든 거(, 같이)
]


@dataclass
class User:
    user_id: int
    first_name: str
    last_name: str


def bad_users_from_rows(dbrows) -> list:
    """DB 로부터 User를 생성하는 그리 좋지 않은 코드"""
    return [User(row[0], row[1], row[2]) for row in dbrows]


def users_from_rows(dbrows) -> list:
    """언패킹의 좋은 사용 예시 (같은 거라도 이게 더 좋은 거라는 말)"""
    return [
        User(user_id, first_name, last_name)
        for (user_id, first_name, last_name) in dbrows
    ]

    return [User(*row) for row in dbrows]  # 결과는 위나 아래나 똑같음


# **사용 예시
"""**는 dict에 사용하면 key를 변수명, value를 변수값으로 사용한다.
        함수인자에 사용하면 들어온 값들을 dict 형식으로 바꿔준다. 
        이는 다양한 임의의 다양한 변수를 허용한다는 의미지만 남용하는 경우 가독성이 떨어지게된다."""


def function(**kwargs):
    print(kwargs)


function(first_param=1, second=2)  # {'first_param': 1, 'second': 2}
