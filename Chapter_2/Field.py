"""field
dataclasses 모듈의 객체
해당 속성에 특별한 특징이 있음을 표시함!

field가 사용되는 것은 Annotation을 함과 동시에 기본값을 할당해주고 싶을 때 사용한다.
단순히 사용하면 class로 인해 생성되는 instance들이 모든 기본 값을 공유하기 때문에 이 기본값이 변경 되었을 때 혼란이 야기될 수 있다.
그렇기에 Annotation과 기본값 설정은 안 되게 설정 되어있고
이를 구현하기 위해 생성시 기본으로 하기 위해 field를 이용해주는 것

물론 그냥 __init__ 함수 안에서 지정해주면 이렇게 할 필요 없음
만약 복잡한 연산이나 validation과정이 필요하면 안 쓰는 게 낫고
그렇게 복잡한 class가 아니라면 편의상 써주는 게 좋을 것같다.
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class TestClass:
    x: int
    y: int
    mylist: list = (
        []
    )  # ValueError: mutable default <class 'list'> for field mylist is not allowed: use default_factory


@dataclass
class FieldClass:
    x: int
    y: int
    mylist: List = field(default_factory=list)


fc = FieldClass(x=1, y=3)
print(fc.x, fc.y, fc.mylist)  # 1 3 []


@dataclass
class WhyWorking:
    x: int
    y: int
    mylist = []


ww = WhyWorking(x=5, y=1)

print(ww.x, ww.y, ww.mylist)  # 5 1 []

ww2 = WhyWorking(x="new", y="new")
print(ww2.x, ww2.y, ww2.mylist)

##예시
R = 26


@dataclass
class TRieNode:
    size = R
    value: int
    next_: List["RTrieNode"] = field(default_factory=lambda: [None] * R)

    def __post_init__(self):
        if len(self.next_) != self.size:
            raise ValueError(f"리스트(next_)의 길이가 유효하지 않음.")
