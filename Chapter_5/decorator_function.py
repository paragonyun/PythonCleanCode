"""데코레이터
데코레이터는 기존의 함수를 포함한 객체를 수정하기 용이하게 만들어주는 기능이다.
데코레이터 이후에 나오는 것을 데코레이터의 첫 번째 파라미터로 적용하고
데코레이터의 결과 값을 반환하게 하는 일종의 Syntax Sugar의 역할을 한다. 

가독성을 크게 높이고, 수정 또한 용이하여 다양하게 사용될 수 있다.
"""
class ControlledException(Exception):
    """도메인의 특정 예외에 대해 특정 횟수만큼 재시도 하는 데코레이터"""

def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        last_raised = None
        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return operation(*args, **kwargs)
            
            except ControlledException as e:
                logger.info(f"{operation.__qualname__} 재시도")
                last_raised = e
        raise last_raised
    
    return wrapped

@retry
def run_operation(task):
    """예외가 일어날 것같은 작업을 실행하고, 예외가 발생하면 retry 데코레이터에 의해 3번 반복"""
    return task.run()

##########################################################################################

class LoginEventSerializer:
    """시스템의 이벤트들의 종류에 따라 전처리를 수행하는 기존의 방식"""
    def __init__(self, event):
        self.event = event

    def serialize(self) -> dict:
        return {
            "username" : self.event.username,
            "password" : "**민감한 정보 삭제**",
            "ip" : self.event.ip,
            "timestamp" : self.event.timestamp.strftime("%Y-%m-%d %H:%M"),
        }

@dataclass
class LoginEvent:
    """이런 식으로 기존의 class를 호출하여 수행"""
    SERIALIZER = LoginEventSerializer

    username: str
    password: str
    ip: str
    timestamp: datetime

    def serialize(self) -> dict:
        return self.SERIALIZER(self).serialize()

"""
-> 이러한 방식은 
1. 클래스 수가 너무 많아진다는 것
2. 유연하지 않다는 것 (패스워드만 숨기고 싶은데 굳이 다른 기능들까지 가져와야 한다.)
3. serialize 함수가 모든 class 안에 있어야 하므로 표준화가 어렵다. 
"""

from datetime import datetime

def hide_field(field) -> str:
    return "**민감한 정보 삭제**"

def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")

def show_original(event_field):
    return event_field

class LoginEventSerializer:
    def __init__(self, serialization_fields: dict) -> None:
        self.serialization_field = serialization_fields

    def serialize(self, event) -> dict:
        return {
            field : transformation(getattr(event, field))
            for field, transformation 
            in self.serialization_field.items()
        }

class Serialization:
    def __init__(self, **transformations):
        self.serializer = LoginEventSerializer(transformations)
    
    def __call__(self, event_class):
        
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)
        
        event_class.serialize = serialize_method
        return event_class

@Serialization(
    username=show_original,
    password=hide_field,
    ip=show_original,
    timestamp=format_time,
)
@dataclass
class LoginEvent:
    username: str
    password: str
    ip: str
    timestamp: datetime
    