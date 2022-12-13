# 🚩 Chapter 1 파이썬스러운(Pythonic) 코드
## 📌 알게된 점
> 1. `__getitem__`을 이용한 자체 Sequence 생성
>
> 2. **Context 괸리자**를 이용하면 순서가 중요한 일과 독립적인 logic이 필요할 때 유용하다.
> 3. **Comprehension**과 **할당식**은 코드를 짧고 빠르게 만들어주지만 그만큼 가독성을 포기해야할 수 있다.
> 4. 내부 메서드는 `_`로 시작한다. `__`의 경우는 class가 속성을 참고할 때 `__attr`로 속성을 만들어 확인하기 때문에 언더바를 2개 사용하는 경우는 지양해야 한다. 
> 5. `property`를 이용하면 `getter`와 `setter`로 validation이 가능하다.
> 6. 간단한 class인 경우 `@dataclass`로 `__init__`없이 구현 가능하다.
> 7. 반복될 대상은 **Iterable**과 **Sequence**가 있다.
>       - Iterable : `__next__`나 `__iter__`를 사용한다. 
>       - Sequence : `__len__`과 `__getitem__`을 사용한다. 
> 8. 포함 관계는 `__contains__`가 유용하다.
> 9. 객체가 속성에 접근하는 방법은 `__getattr__`로 정의한다.
> 10. 객체가 호출될 때의 행동은 `__call__`로 정의한다. 
> 11. **Mutable**객체는 함수의 기본인자로 사용하지 않는다.


<br>

<br>

## 👀 사용 예시
유용했던 것만 정리하고자 한다.

**`__call__`**
```python
from collections import defaultdict


class CallCount:
    def __init__(
        self,
    ):
        self._counts = defaultdict(int)

    def __call__(self, arg):
        """호출되면 arg의 count 횟수를 1 추가하고 반환합니다."""
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


## __getattr__ 예시
class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):  ## 기존에 등록되어 있지 않는 속성(attr)이 들어왔을 때 아래와 같이 처리한다.
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "")
            return f"[fallback resolved] {name}"
        raise AttributeError(f"{self.__class__.__name__}에는 {attr} 속성이 존재하지 않습니다.")


dyn = DynamicAttributes("value")
print(dyn.attribute)  # value, 정상 작동

# fallback_으로 시작하는 새로운 attribute가 들어온 경우
print(dyn.fallback_test)  # [fallback resolved] test

# 아예 새로운 attribute가 들어온 경우
# print(dyn.completely_new_value) # AttributeError: DynamicAttributes에는 completely_new_value 속성이 존재하지 않습니다.

# 새로운 속성을 추가하는 경우
dyn.__dict__["Something_NEW"] = "this is something new attr"
print(dyn.Something_NEW)  # this is something new attr


# getattr 함수는 에러가 발생하는 경우 3번째 인자를 반환한다.
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
    ):  # __contains__를 통해 x와 y가 width와 height 안에 있는지 T/F로 return 한다.
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(
            width, height
        )  # 아까 만들어둔 class를 통해 width와 hegith 안에 corrd가 존재하는지 확인 가능

    def __contains__(self, coord):
        return coord in self.limits


"""두 class는 매우 응집력 있으며 최소한의 logic, 간결하고 자명한 메서드, 적절한 객체명을 가지고 있다. 매우 파이써닉!"""


# 활용예시
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
            raise ValueError(f"유효하지 않은 위도 값입니다. : {lat_value}")
        self._latitude = lat_value

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if long_value not in range(-180, 180 + 1):
            raise ValueError(f"유효하지 않은 위도 값입니다. : {long_value}")
        self._longitude = long_value


coo = Coordinate(10.20, 10.10)
print("처음 값")
print(coo.latitude, coo.longitude)

try:
    coo.longitude = 1000.01  # 에러발생
except:
    coo.longitude = 100.02  # 통과
print("변경 후")
print(coo.latitude, coo.longitude)
```