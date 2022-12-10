"""
파이썬의 모든 객체는 public 속성
_name() 등으로 호출을 안 하길 기대할 수 있지만 강제할 수는 없다.

Name Mangling (이름 맹글링)
__을 사용한 변수의 이름을 "_<class이름>__<arribute이름>" 으로 바꿔주는 역할을 한다.
__는 여러 번 확장되는 클래스 메서드를 충돌 없이 오버라이드 시키기 위해 만들어졌다. 
때문에 쓸 데 없는 __의 이름을 바꿔버리는 것
"""


class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60
        self.__cannotcall = "Hi"


conn = Connector("Source")
print(conn.source)
print(conn._timeout)  # _로 표시했지만 호출할 수 있다.
print(conn.__dict__)  # __dict__는 init에 표시된 생성자를 모두 확인할 수 있다.
try:
    print(conn.__cannotcall)  # __로 표시된 것은 표시할 수 없다.
except:
    print(conn._Connector__cannotcall)  # 이렇게 해야 표시할 수 있다.
