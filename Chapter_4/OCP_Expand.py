"""잘 만들어진 OCP예시에 새로운 이벤트가 추가되는 경우
기존의 구조에 Transaction이라는 이벤트가 추가된다고 해보자

그냥 아래의 class 하나만 추가해주면 된다. 기존의 메서드를 수정해줄 필요도 없음!!
"""
from .OCP_Good import *


class TransactionEvent(Event):
    """새로 추가된 이벤트 유형"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["after"].get("transaction") is not None
