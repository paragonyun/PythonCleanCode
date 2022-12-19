# 🚩 Chapter 3 좋은 코드의 일반적인 특징
## 📌 알게된 점
> 1. **문제가 되는 부분을 효율적으로 탐지하기 위해 `DbC`가 활용된다.**
>       - 사전, 사후 조건으로 문제가 되는 지점을 명확하게 한다.
> 2. **방어적 프로그래밍은 함수, 코드가 유효하지 않은 값들로부터 보호하게 하기 위함이다.**
>       - 값대체, 예외처리, `assert`
> 3. **기능과 책임의 분리는 명확해야 한다.**
>       - 좋은 프로그램은 _응집력이 높고 결합력은 낮다._
> 4. 개발지침 약어는 알아두면 좋다. (DRY, OOAO, YAGNI, KIS, EAFP, LBYL)
> 5. 상속의 메서드 결정순서를 이해하면 mixin도 활용 가능하다.
> 6. 함수의 인자를 어떻게 다루느냐에 따라 보편성이 좋아지기도 하지만 가독성이 떨어질 수 있다.
>       - `*arg`, `**kwarg`, mutable, packing, unpacking
> 7. 함수의 인자가 너무 많으면 객체화 하는 방안을 생각해보자.
>
> 8. (제일 중요)**함수는 한가지 일만 해야한다!!!**


<br>

<br>

## 👀 사용 예시

**소프트웨어의 독립성**
```python
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
```

<br>

**Mutable**
```python
def function(arg):
    arg += " in function"
    print(arg)


immutable = "hello"
function(immutable)  # hello in function | hello는 변하지 않는 값이다.
mutable = list("hello")
function(mutable) # ['h', 'e', 'l', 'l', 'o', ' ', 'i', 'n', ' ', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n'] 이때의 hello는 list로 변할 수 있는 값이 된다.

print(
    f"function 함수 이후의 값\nimmutable:hello->{immutable}\nmutable:{list('hello')}->{mutable}"
) 
# function 함수 이후의 값
# immutable:hello->hello
# mutable:['h', 'e', 'l', 'l', 'o']->['h', 'e', 'l', 'l', 'o', ' ', 'i', 'n', ' ', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n']
```