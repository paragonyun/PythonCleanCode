"""방어적 프로그래밍
애초에 에러가 발생하지 않거나 유효하지 않은 값들로부터 함수나 객체가 스스로 보호하게 하는 것
쉽게 말해, x를 원하는데 y가 들어온 경우 어떻게 할지를 논의하는 것이다.
주로 에러를 어떻게 처리할 것인지 (default 값으로 대체, try exeption) 
아예 그 값을 받지 못하게 할 것인지 (assert)
에 대해 다루게 된다.

- 너무 많은 Exception은 해당 함수가 좋지 않음을 의미한다.
    - 올바른 수준의 추상화 단계에서의 예외 처리
        예외는 한 가지 일을 하는 함수의 한 부분이어야 한다.
        즉, 다른 함수의 역할을 가지고 해당 함수에서 예외를 발생시키지 말라는 것
"""
## 올바른 수준의 추상화 단계에서의 예외 처리
class DataTransport:
    """다양한 수준의 예외 처리 예시"""

    _RETRY_BACKOFF: int = 5
    _RETRY_TIMES: int = 3

    def __init__(self, connector: Connector) -> None:
        self._connector = connector
        self.connection = None

    def deliver_event(self, event: Event):
        try:
            self.connect()
            data = event.decode()
            self.send(data)
        except ConnectionError as e:
            logger.info(f"커넥션 오류 발견: {e}")
            raise
        except ValueError as e:
            logger.error(f"{event}에 잘못된 데이터가 들어옴: {e}")
            raise

    def connect(self):
        for _ in range(self._RETRY_TIMES):
            try:
                self.connection = self._connector.connect()
            except ConnectionError as e:
                logger.info(f"{e}: 새로운 커넥션 시도 {self._RETRY_BACKOFF}")
                time.sleep(self._RETRY_BACKOFF)
            else:
                return self.connection

        raise ConnectionError(f"연결 실패 | 재시도 횟수 : {self._RETRY_TIMES}번")

    def send(self, data: bytes):
        return self.connection.send(data)

    """Value Error와 ConnectionError는 서로 관계가 없음에도 불구하고 
        같은 메서드 안에 존재함. 이는 혼란을 야기하며 곧 해당 함수가 너무 많은 기능을
        담당하고 있음을 의미하기도 한다."""


def connect_with_retry(
    connector: Connector, retry_n_times: int, retry_backoff: int = 5
):
    """위의 deliver 함수의 기능 중 연결 재시도 기능을 분리"""
    for _ in range(retry_n_times):
        try:
            return connector.connect()
        except ConnectionError as e:
            logger.info(f"{e}: 연결 실패 | {retry_backoff}초 후에 연결 재시도")
            time.sleep(retry_backoff)

        exc = ConnectionError(f"연결 실패 ({retry_n_times}회 재시도)")
        logger.exeption(exc)
        return exc


class ModifiedClass:
    """기능을 적절히 분리 시킨 객체"""

    _RETRY_BACKOFF: int = 5
    _RETRY_TIMES: int = 3

    def __init__(self, connector: Connector) -> None:
        self._connector = connector
        self.connection = None

    def deliver_event(self, event: Event):
        self.connection = connect_with_retry(
            self._connector, self._RETRY_TIMES, self._RETRY_BACKOFF
        )
        self.send(event)

    def send(self, event: Event):
        try:
            return self.connection.send(event.decode)
        except ValueError as e:
            logger.error(f"{event} 잘못된 데이터 포함: {e}")
            raise

    """이제 각 기능과 관심사가 분리되어 있는 함수의 조합으로 이루어졌다."""


## Error 메세지 커스텀하기
class InternalDataError(Exeption):
    """raise <e> from <original>"""

    def process(data_dictionary, record_id):
        try:
            return data_dictionary[record_id]

        except KeyError as e:
            raise InternalDataError("데이터가 없습니다.") from e


def assert_test(x: int, y: int):
    assert x < 10 and y > 10
    return x * y


print(assert_test(11, 5))  # AssertionError
