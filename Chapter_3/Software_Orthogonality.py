"""결론
1. 소프트웨어의 독립성
    - 내부적인 함수와 메서드들은 서로 영향을 미치면 안 된다는 것. 
    - 그 안에서만 영향을 미쳐야 한다
    항상 강조됐던 내용임과 동시에 이 책에서 말하고자 하는 중요한 포인트

2. 코드 구조
    - 여러 정의가 들어가있는 큰 파일을 만드는 것은 좋지 않다.
    - 유사한 기능을 하는 파일들만 .py로 만들어 관리하는 것이 유리하다. 
"""

## 독립성
"""위의 두개 함수는 독립성을 가짐. 즉, 하나를 변경해도 하나는 변경되지 않음.
    마지막 함수는 함수를 지정하지 않으면 str을 기본으로 사용하고 함수를 전달하면 해당 형태로 전달함.
    그러나 show_price의 수정은 calculate 함수에 영향을 주지 않음!!!"""


def calculate_price(base_price: float, tax: float, discount: float) -> float:
    return (base_price * (1 + tax)) * (1 - discount)


def show_price(price: float) -> str:
    return f"💸 {price:.2f}"


def str_final_price(
    base_price: float, tax: float, discount: float, fmt_function=str
) -> str:
    return fmt_function(calculate_price(base_price, tax, discount))


print(str_final_price(10, 0.2, 0.5))  # 6.0
print(str_final_price(10, 0.2, 0.5, fmt_function=show_price))  # 💸 6.00
