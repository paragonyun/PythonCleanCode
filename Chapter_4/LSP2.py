from collections.abc import Mapping


class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False

    @staticmethod
    def validate_precondition(event_data: dict):
        """인터페이스 계약의 사전조건을 정의
        'event_data'의 파라미터가 적절한 형태인지 확인하는 부분
        """
        if not isinstance(event_data, Mapping):
            raise ValueError(f"{event_data!r} dict 데이터 타입이 아닙니다.")
        for moment in ("before", "after"):
            if moment not in event_data:
                raise ValueError(f"{event_data}에 {moment} 정보가 없습니다.")

            if not isinstance(event_data[moment], Mapping):
                raise ValueError(f"event_data[{moment!r}] dict 데이터 타입이 아닙니다.")


class SystemMonitor:
    """시스템에서 발생한 이벤트를 분류하는 곳"""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        Event.validate_precondition(self.event_data)  ## 일단 먼저 확인
        event_cls = next(
            (
                event_cls
                for event_cls in Event.__subclasses__()
                if event_cls.meets_condition(self.event_data)
            ),
            UnknownEvent,
        )
        return event_cls(self.event_data)


class TransactionEvent(Event):
    """시스템에서 발생한 Transaction 관련 이벤트"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["after"].get("transaction") is not None
