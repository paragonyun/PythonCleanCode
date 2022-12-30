# 🚩 Chapter 4 SOLID 원칙
## 📌 알게된 점
> 1. **SOLID 원칙**은 필수적인 것은 아니지만 미래의 유지보수가 원활하게 하는 디자인 방법이다.
> 
> 2. **`SRP(단일책임원칙)`** : 모든 Class는 하나의 책임(기능)만을 가지고 있어야 한다.
>       - 너무 많은 책임은 많은 수정이 요구된다.
>       - 꼭 Class당 기능이 1개여야 한다는 것은 아니고, Logic에 필요한 최소한의 기능만을 갖추어야 한다는 의미다.
> 3. **`OCP(개방폐쇄의 원칙)`** : Class는 캡슐화된 Logic으로 이루어져야 하며 **수정엔 폐쇄적이고 확장엔 개방적이어야 한다.** 
>       - 기존의 것을 수정할 필요가 없도록 설계해야 한다는 의미다.
> 4. **`LIP(리스코프 치환)`** : 부모 Class에 대해 모르고 있어도 사용에는 문제가 없어야 한다.
>       - 올바른 계층구조 설계에 대한 것이다.
> 5. **`ISP(인터페이스 분리)`** : SRP와 비슷하게 인터페이스의 기능을 분리해야 한다는 의미이다.
>       - 작은 인터페이스를 지향한다.
> 6. **`DIP(의존성 역전)`** : 코드는 다른 코드에 너무 과하게 의존해선 안 된다. 
>       - 핵심은 한 코드 내에서 필요한 기능이나 요소를 생성하는 것이 아닌, 제공을 받자는 것이다.


<br>

<br>

## 👀 사용 예시

**OCP** (개인적으로 가장 기발하다고 생각했다.)
```python
class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False


class UnkownEvent(Event):
    """아까와 같은 상황일 때"""


class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
            event_data["before"]["session"] == 0
            and event_data["before"]["session"] == 1
        )


class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
            event_data["before"]["session"] == 1
            and event_data["before"]["session"] == 0
        )


class SystemMonitor:
    """여기서 분류"""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):  ## 이게 True를 반환하면
                    return event_cls(self.event_data)  ## 해당 조건 반환

            except KeyError:
                continue

        return UnkownEvent(self.event_data)
```

<br>

**DIP**
```python
class EventStreamer:
    """의존성 주입 전
    단위 테스트를 할 때도 Syslog를 수정해야 하고 만약 syslog에 문제가 있다면 
    그 문제가 초기화 할 때 그대로 발생함
    (애초에 init 에서 무언가를 생성하는 것을 권장하지는 않음)
    """
    def __init__(self):
        self._target = Syslog()

    def stream(self, events: list[Event]) -> None:
        for event in events:
            self._target.send(event.serialise())

class EventStreamer:
    """의존성 주입 후
    직접 관리하는 것이 아닌 필요한 정보를 제공받는 것
    
    이렇게 하면 초기화 시 다양한 객체 전달이 가능하고 테스트도 더 간단해졌음
    """
    def __init__(self, target: DataTargetClient):
        self._target = target

    def stream(self, events: list[Event]) -> None:
        for event in events:
            self._target.send(event.serialise())
```