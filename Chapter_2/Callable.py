"""Callable
함수처럼 작동하는 객체. 딥러닝에서 흔히 활용했던 Early Stopping 기능같은 경우도 __call__ 메서드를 적극적으로 활용한 결과다.

객체를 호출하면 기본적으로 __call__ 메서드가 호출된다.
이때, 객체를 호출할 때 상요했던 파라미터는 __call__에 모두 전달된다.

기본적으로 객체는 상태를 저장할 수 있다. 호출이 일어날 때 알맞은 정보를 저장해두고
이를 나중에 활용할 수 있다는 것.

즉, 어떤 기능을 호출할 때마다 관리해야하는 상태가 있다면, 부를 때마다 어떤 기능을 하는 호출형 객체를 쓰는 게 더 편하다는 것

우리가  class를 만들 때 class(x, y)로 만들면 기본적으로 class.__call__(x, y) 형태로 변환한다.
"""
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
