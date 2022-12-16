"""개발지침약어
1. DRY(Do not Repeat Yourself) / OAOO(Once And Only Once)
    - 코드의 중복은 반드시 피하고, 중복이 발생하면 함수화를 시켜 극복하자!
2. YAGNI(You Ain't Gonna Need It)
    - 너무 미래를 생각해서 복잡한 기능을 구현하지 말자.
    - 현재에 필요한 기능 개발에 집중해라!
3. KIS(Keep It Simple)
    - 디자인은 최대한 간단해야 한다.
4. EAFP(Easier to Ask Forgiveness than Permission) / LBYL(Look Before You Leap)
    - EAFP : 일단 코드를 작성해보고 동작하지 않을 때 대응한다는 말.
    - LBYL : 파일을 사용하기 전에 사용할 수 있는지 확인하라는 말
    - 보통 EAFP 방식을 선택 => try except로 코드 구분괴 에러 발생 가능성이 더 낮기 때문

"""
## KIS 예시
class ComplicatedNamespace:
    """복잡하게 초기화 하는 예시"""

    ACCEPTED_VALUES = ("id_", "user", "location")

    @classmethod
    def init_with_data(cls, **data):
        instance = cls()
        for key, value in data.items():
            if key in cls.ACCEPTED_VALUES:
                setattr(instance, key, value)
        return instance


cn = ComplicatedNamespace.init_with_data(
    id_=42, user="root", location="127.0.0.1", extra="excluded"
)
print(cn.id_, cn.user, cn.location)  # 42 root 127.0.0.1


class SimpleNamespace:
    """__init__으로 간단하게 초기화"""

    ACCEPTED_VALUES = ("id_", "user", "location")

    def __init__(self, **data):
        for attr_name, attr_value in data.items():
            if attr_name in self.ACCEPTED_VALUES:
                setattr(self, attr_name, attr_value)
