# ๐ฉ Chapter 3 ์ข์ ์ฝ๋์ ์ผ๋ฐ์ ์ธ ํน์ง
## ๐ ์๊ฒ๋ ์ 
> 1. **๋ฌธ์ ๊ฐ ๋๋ ๋ถ๋ถ์ ํจ์จ์ ์ผ๋ก ํ์งํ๊ธฐ ์ํด `DbC`๊ฐ ํ์ฉ๋๋ค.**
>       - ์ฌ์ , ์ฌํ ์กฐ๊ฑด์ผ๋ก ๋ฌธ์ ๊ฐ ๋๋ ์ง์ ์ ๋ชํํ๊ฒ ํ๋ค.
> 2. **๋ฐฉ์ด์  ํ๋ก๊ทธ๋๋ฐ์ ํจ์, ์ฝ๋๊ฐ ์ ํจํ์ง ์์ ๊ฐ๋ค๋ก๋ถํฐ ๋ณดํธํ๊ฒ ํ๊ธฐ ์ํจ์ด๋ค.**
>       - ๊ฐ๋์ฒด, ์์ธ์ฒ๋ฆฌ, `assert`
> 3. **๊ธฐ๋ฅ๊ณผ ์ฑ์์ ๋ถ๋ฆฌ๋ ๋ชํํด์ผ ํ๋ค.**
>       - ์ข์ ํ๋ก๊ทธ๋จ์ _์์ง๋ ฅ์ด ๋๊ณ  ๊ฒฐํฉ๋ ฅ์ ๋ฎ๋ค._
> 4. ๊ฐ๋ฐ์ง์นจ ์ฝ์ด๋ ์์๋๋ฉด ์ข๋ค. (DRY, OOAO, YAGNI, KIS, EAFP, LBYL)
> 5. ์์์ ๋ฉ์๋ ๊ฒฐ์ ์์๋ฅผ ์ดํดํ๋ฉด mixin๋ ํ์ฉ ๊ฐ๋ฅํ๋ค.
> 6. ํจ์์ ์ธ์๋ฅผ ์ด๋ป๊ฒ ๋ค๋ฃจ๋๋์ ๋ฐ๋ผ ๋ณดํธ์ฑ์ด ์ข์์ง๊ธฐ๋ ํ์ง๋ง ๊ฐ๋์ฑ์ด ๋จ์ด์ง ์ ์๋ค.
>       - `*arg`, `**kwarg`, mutable, packing, unpacking
> 7. ํจ์์ ์ธ์๊ฐ ๋๋ฌด ๋ง์ผ๋ฉด ๊ฐ์ฒดํ ํ๋ ๋ฐฉ์์ ์๊ฐํด๋ณด์.
>
> 8. (์ ์ผ ์ค์)**ํจ์๋ ํ๊ฐ์ง ์ผ๋ง ํด์ผํ๋ค!!!**


<br>

<br>

## ๐ ์ฌ์ฉ ์์

**์ํํธ์จ์ด์ ๋๋ฆฝ์ฑ**
```python
def calculate_price(base_price: float, tax: float, discount: float) -> float:
    return (base_price * (1 + tax)) * (1 - discount)


def show_price(price: float) -> str:
    return f"๐ธ {price:.2f}"


def str_final_price(
    base_price: float, tax: float, discount: float, fmt_function=str
) -> str:
    return fmt_function(calculate_price(base_price, tax, discount))


print(str_final_price(10, 0.2, 0.5))  # 6.0
print(str_final_price(10, 0.2, 0.5, fmt_function=show_price))  # ๐ธ 6.00
```

<br>

**Mutable**
```python
def function(arg):
    arg += " in function"
    print(arg)


immutable = "hello"
function(immutable)  # hello in function | hello๋ ๋ณํ์ง ์๋ ๊ฐ์ด๋ค.
mutable = list("hello")
function(mutable) # ['h', 'e', 'l', 'l', 'o', ' ', 'i', 'n', ' ', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n'] ์ด๋์ hello๋ list๋ก ๋ณํ  ์ ์๋ ๊ฐ์ด ๋๋ค.

print(
    f"function ํจ์ ์ดํ์ ๊ฐ\nimmutable:hello->{immutable}\nmutable:{list('hello')}->{mutable}"
) 
# function ํจ์ ์ดํ์ ๊ฐ
# immutable:hello->hello
# mutable:['h', 'e', 'l', 'l', 'o']->['h', 'e', 'l', 'l', 'o', ' ', 'i', 'n', ' ', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n']
```