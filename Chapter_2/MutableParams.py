"""변경 가능한 파라미터의 기본값
함수의 기본 인자로 변경 가능한 객체를 쓰면 안 된다는 말이다.
"""


def wrong_case(user_data: dict = {"name": "Midal", "age": 23}):

    name = user_data.pop("name")
    age = user_data.pop("age")

    print(f"{name} ({age}세)")


# 첫번째 호출
wrong_case()  # Midal (23세)
"""여기서 내부의 pop으로 인해 기본 인자로 들어간 dict의 name과 age 키는 사라진다."""

# 두번째 호출
wrong_case()  # KeyError: 'name'

## 아래와 같은 걸로 극복 가능하긴 함
def advised_case(user_data: dict = None):
    user_data = user_data or {"name": "Midal", "age": 23}

    name = user_data.pop("name")
    age = user_data.pop("age")

    print(f"{name} ({age}세)")


# 첫번째 호출
advised_case()  # Midal (23세)

# 두번째 호출
advised_case()  # Midal (23세)
