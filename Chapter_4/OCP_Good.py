"""OCP좋은 예시
아예 class 내부에서 해당 조건을 만족하는지 아닌지를 return 하는 메서드를 만들고
identify 메서드는 이들을 돌면서 확인하는 용도로만 사용
이렇게 하면 새로운 이벤트가 추가되더라도 identify 메서드는 수정할 필요가 없어진다!!
와우 대박...
정말 깔끔하고 좋은 코드인 것같다. 이렇게 할 수 있는 생각을 많이 해야겠다.. 
"""


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
