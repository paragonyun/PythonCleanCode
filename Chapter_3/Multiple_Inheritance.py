"""다중상속
- 메서드 결정 순서(MRO)
    - 다이아몬드 문제가 발생할 수 있다. 예를 들어, 최상위 클래스와 부모 클래스가 같은 이름의 메서드를 가질 때,
        손자 클래스틑 어떤 메서드를 써야하는지에 대한 문제다.
    -  MRO 알고리즘은 가장 가까운 순서대로 사용한다.

- 믹스인(Mixin)
    - 코드를 재사용하기 위해 일반적인 행동을 캡슐화한 부모 클래스
    - 대부분 달느 클래스의 매서드나 속성과 결합하여 사용하기 때문에 혼자만으로는 유용하지 않은 편이다.
    - 보통은 믹스인 클래스와 다른 클래스를 다중 상속하고 믹스인 클래스의 메서드와 속성을 다른 클레스에서 사용한다.
"""
## 메서드 결정 순서 확인
class GrandModule:
    module_name = "top"

    def __init__(self, module_name):
        self.name = module_name

    def __str__(self):
        return f"{self.module_name} : {self.name}"


class ChildModule1(GrandModule):
    module_name = "module-1"


class ChildModule2(GrandModule):
    module_name = "module-2"


class ChildModule3(GrandModule):
    module_name = "module-3"


class GrandChildModule1(ChildModule1, ChildModule2):
    """1번 자식 클래스와 2번 자식 클래스의 확장"""


class GrandChildModule2(ChildModule2, ChildModule3):
    """2번 자식 클래스와 3번 자식 클래스의 확장"""


"""각자 앞에 있는 걸 불러옴"""
print(str(GrandChildModule1("test")))  # module-1 : test
print(str(GrandChildModule2("test")))  # module-2 : test
module_seq = [
    cls.__name__ for cls in GrandChildModule1.mro()
]  # MRO 알고리즘에 의한 호출 순서 파악 가능!
print(
    module_seq
)  # ['GrandChildModule1', 'ChildModule1', 'ChildModule2', 'GrandModule', 'object']

## Minin Clasfs
"""문자열을 받아 하이픈으로 구분하는 class"""


class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(
        self,
    ):
        yield from self.str_token.split(
            "-"
        )  ## https://dojang.io/mod/page/view.php?id=2414 여기서 해당 문법 참고.


tk = BaseTokenizer("1531-dfh5458-12d3af84-love")
print(list(tk))  # ['1531', 'dfh5458', '12d3af84', 'love']

"""대문자로 바꿔주는 class"""


class UpperMakerMixin:
    def __iter__(self):
        return map(
            str.upper, super().__iter__()
        )  ## __iter__를 호출하고 super()를 통해 변환을 마친 다음 Base에 전달하게됨


class Tokenizer(UpperMakerMixin, BaseTokenizer):  ## 이렇게 하면 데코레이터의 역할과 같음
    pass


tk2 = Tokenizer("1531-dfh5458-12d3af84-love")
print(list(tk2))  # ['1531', 'DFH5458', '12D3AF84', 'LOVE']
