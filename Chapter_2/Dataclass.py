"""
@dataclass는 자체적으로 __init__에서 정의한 것처럼 모든 인스턴스를 처리한다.
"""

# @dataclass적용 예시
from dataclasses import dataclass


class TestClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


test = TestClass(x=1, y=2)
print(test.x, test.y)


@dataclass
class DataClass:
    x: float
    y: int


dataclass = DataClass(x=1.5, y=4)
print(dataclass.x, dataclass.y)
