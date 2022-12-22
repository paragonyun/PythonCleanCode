"""mypy를 통한 LSP 준수여부 확인

"""


class Event:
    def meets_condition(self, event_data: dict) -> bool:
        return False


class LoginEvent(Event):
    """하위 클래스가 호환되지 않는 방식으로 메서드를 정의한 경우
    부모 클래스는 dict를 받지만 자식 클래스는 list를 받는다.
    """

    def meets_condition(self, event_data: list) -> bool:
        return bool(event_data)

    """mypy 실행 결과
    LSP_mypy.py:12: error: Argument 1 of "meets_condition" is incompatible with supertype "Event"; supertype defines the argument type as "Dict[Any, Any]"  [override]
    """
