# ๐ฉ Chapter 2 ํ์ด์ฌ์ค๋ฌ์ด(Pythonic) ์ฝ๋
## ๐ ์๊ฒ๋ ์ 
> 1. `__getitem__`์ ์ด์ฉํ ์์ฒด Sequence ์์ฑ
>
> 2. **Context ๊ดธ๋ฆฌ์**๋ฅผ ์ด์ฉํ๋ฉด ์์๊ฐ ์ค์ํ ์ผ๊ณผ ๋๋ฆฝ์ ์ธ logic์ด ํ์ํ  ๋ ์ ์ฉํ๋ค.
> 3. **Comprehension**๊ณผ **ํ ๋น์**์ ์ฝ๋๋ฅผ ์งง๊ณ  ๋น ๋ฅด๊ฒ ๋ง๋ค์ด์ฃผ์ง๋ง ๊ทธ๋งํผ ๊ฐ๋์ฑ์ ํฌ๊ธฐํด์ผํ  ์ ์๋ค.
> 4. ๋ด๋ถ ๋ฉ์๋๋ `_`๋ก ์์ํ๋ค. `__`์ ๊ฒฝ์ฐ๋ class๊ฐ ์์ฑ์ ์ฐธ๊ณ ํ  ๋ `__attr`๋ก ์์ฑ์ ๋ง๋ค์ด ํ์ธํ๊ธฐ ๋๋ฌธ์ ์ธ๋๋ฐ๋ฅผ 2๊ฐ ์ฌ์ฉํ๋ ๊ฒฝ์ฐ๋ ์ง์ํด์ผ ํ๋ค. 
> 5. `property`๋ฅผ ์ด์ฉํ๋ฉด `getter`์ `setter`๋ก validation์ด ๊ฐ๋ฅํ๋ค.
> 6. ๊ฐ๋จํ class์ธ ๊ฒฝ์ฐ `@dataclass`๋ก `__init__`์์ด ๊ตฌํ ๊ฐ๋ฅํ๋ค.
> 7. ๋ฐ๋ณต๋  ๋์์ **Iterable**๊ณผ **Sequence**๊ฐ ์๋ค.
>       - Iterable : `__next__`๋ `__iter__`๋ฅผ ์ฌ์ฉํ๋ค. 
>       - Sequence : `__len__`๊ณผ `__getitem__`์ ์ฌ์ฉํ๋ค. 
> 8. ํฌํจ ๊ด๊ณ๋ `__contains__`๊ฐ ์ ์ฉํ๋ค.
> 9. ๊ฐ์ฒด๊ฐ ์์ฑ์ ์ ๊ทผํ๋ ๋ฐฉ๋ฒ์ `__getattr__`๋ก ์ ์ํ๋ค.
> 10. ๊ฐ์ฒด๊ฐ ํธ์ถ๋  ๋์ ํ๋์ `__call__`๋ก ์ ์ํ๋ค. 
> 11. **Mutable**๊ฐ์ฒด๋ ํจ์์ ๊ธฐ๋ณธ์ธ์๋ก ์ฌ์ฉํ์ง ์๋๋ค.


<br>

<br>

## ๐ ์ฌ์ฉ ์์
์ ์ฉํ๋ ๊ฒ๋ง ์ ๋ฆฌํ๊ณ ์ ํ๋ค.

**`__call__`**
```python
from collections import defaultdict


class CallCount:
    def __init__(
        self,
    ):
        self._counts = defaultdict(int)

    def __call__(self, arg):
        """ํธ์ถ๋๋ฉด arg์ count ํ์๋ฅผ 1 ์ถ๊ฐํ๊ณ  ๋ฐํํฉ๋๋ค."""
        self._counts[arg] += 1
        return self._counts[arg]


cc = CallCount()
print(cc(1))  # 1
print(cc(2))  # 1
print(cc(3))  # 1
print(cc(4))  # 1
print(cc(1))  # 2
print(cc(3))  # 2
```

<br>

**`__getattr__`**
```python
class DictCase:
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = DictCase(x=1, y=2)
a.z = 3
print(a.z)  # 3

b = DictCase(x=1, y=2)
# print(b.z) # AttributeError: 'DictCase' object has no attribute 'z'


## __getattr__ ์์
class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):  ## ๊ธฐ์กด์ ๋ฑ๋ก๋์ด ์์ง ์๋ ์์ฑ(attr)์ด ๋ค์ด์์ ๋ ์๋์ ๊ฐ์ด ์ฒ๋ฆฌํ๋ค.
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "")
            return f"[fallback resolved] {name}"
        raise AttributeError(f"{self.__class__.__name__}์๋ {attr} ์์ฑ์ด ์กด์ฌํ์ง ์์ต๋๋ค.")


dyn = DynamicAttributes("value")
print(dyn.attribute)  # value, ์ ์ ์๋

# fallback_์ผ๋ก ์์ํ๋ ์๋ก์ด attribute๊ฐ ๋ค์ด์จ ๊ฒฝ์ฐ
print(dyn.fallback_test)  # [fallback resolved] test

# ์์ ์๋ก์ด attribute๊ฐ ๋ค์ด์จ ๊ฒฝ์ฐ
# print(dyn.completely_new_value) # AttributeError: DynamicAttributes์๋ completely_new_value ์์ฑ์ด ์กด์ฌํ์ง ์์ต๋๋ค.

# ์๋ก์ด ์์ฑ์ ์ถ๊ฐํ๋ ๊ฒฝ์ฐ
dyn.__dict__["Something_NEW"] = "this is something new attr"
print(dyn.Something_NEW)  # this is something new attr


# getattr ํจ์๋ ์๋ฌ๊ฐ ๋ฐ์ํ๋ ๊ฒฝ์ฐ 3๋ฒ์งธ ์ธ์๋ฅผ ๋ฐํํ๋ค.
print(getattr(dyn, "somthing", "new"))  # new
```

<br>

**`__contains__`**
```python
## Bad Case
def mark_coordinate(grid, coord):
    if 0 <= coord.x < grid.width and 0 <= coord.y < grid.hegith:
        grid[coord] = 1


## Good CAse
class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(
        self, coord
    ):  # __contains__๋ฅผ ํตํด x์ y๊ฐ width์ height ์์ ์๋์ง T/F๋ก return ํ๋ค.
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(
            width, height
        )  # ์๊น ๋ง๋ค์ด๋ class๋ฅผ ํตํด width์ hegith ์์ corrd๊ฐ ์กด์ฌํ๋์ง ํ์ธ ๊ฐ๋ฅ

    def __contains__(self, coord):
        return coord in self.limits


"""๋ class๋ ๋งค์ฐ ์์ง๋ ฅ ์์ผ๋ฉฐ ์ต์ํ์ logic, ๊ฐ๊ฒฐํ๊ณ  ์๋ชํ ๋ฉ์๋, ์ ์ ํ ๊ฐ์ฒด๋ช์ ๊ฐ์ง๊ณ  ์๋ค. ๋งค์ฐ ํ์ด์จ๋!"""


# ํ์ฉ์์
def mark_coordinate(grid, coord):
    if coord in grid:
        grid[coord] = 2
```

<br>

**`@property`**
```python
class Coordinate:
    def __init__(self, lat: float, long: float) -> None:
        self._latitude = self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if lat_value not in range(-90, 90 + 1):
            raise ValueError(f"์ ํจํ์ง ์์ ์๋ ๊ฐ์๋๋ค. : {lat_value}")
        self._latitude = lat_value

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if long_value not in range(-180, 180 + 1):
            raise ValueError(f"์ ํจํ์ง ์์ ์๋ ๊ฐ์๋๋ค. : {long_value}")
        self._longitude = long_value


coo = Coordinate(10.20, 10.10)
print("์ฒ์ ๊ฐ")
print(coo.latitude, coo.longitude)

try:
    coo.longitude = 1000.01  # ์๋ฌ๋ฐ์
except:
    coo.longitude = 100.02  # ํต๊ณผ
print("๋ณ๊ฒฝ ํ")
print(coo.latitude, coo.longitude)
```