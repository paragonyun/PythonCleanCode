"""OCP를 지키지 않은 예시
수집된 데이터를 바탕으로 이벤트 타입을 나누는 시스템을 개발했다고 하자.
session이 0이었다가 1이면 로그인 이벤트로, 1이었다가 0이되면 로그아웃 이벤트로 분류한다.
나머진 Unkown으로 분류한다.

이 예시는 유형을 결정하는 로직이 identify_event 메서드에 집중된다는 것이다.
이런 경우엔 추가적으로 다른 유형의 이벤트가 추가될 때, 계속해서 elif로 늘어뜨려야 하는
보기 싫은 상황이 연출될 수 있다.
"""


from dataclasses import dataclass


@dataclass
class Event:
    raw_data: dict


class UnknownEvent(Event):
    """구별 불가능한 데이터"""


class LoginEvent(Event):
    """로그인한 사용자가 남긴 이벤트"""


class LogoutEvent(Event):
    """로그아웃 사용자가 남긴 이벤트"""


class SystemMonitor:
    """시스템에서 발생한 이벤트를 분류"""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        """이벤트를 구분하는 메서드"""
        if (
            self.event_data["before"]["session"] == 0
            and self.event_data["before"]["session"] == 1
        ):
            return LoginEvent(self.event_data)

        elif (
            self.event_data["before"]["session"] == 1
            and self.event_data["before"]["session"] == 0
        ):
            return LogoutEvent(self.event_data)

        return UnknownEvent(self.event_data)
