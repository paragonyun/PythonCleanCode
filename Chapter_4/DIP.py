"""의존성 역전 원칙
코드가 깨지거나 손상되는 취약점으로부터 보호해주는 원칙
-> 코드가 세부사항이나 구체적으니 구현에 적응하도록 하지 않게 하는 것!!

=> 의존성 주입
    - 코드가 구체적인 특정 구현에 종속되게 하지 말고, 계층 사이를 연결하는 강력한 추상화 개체와 이야기 하게 만드는 것
    - 필수는 아니지만 모델에 대한 가독성이 높아짐
    - 직관적으로는,,, 내부에서 필요한 것을 만들지 말고 "제공 받는 형태"로 만드는 것을 의미
"""
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
