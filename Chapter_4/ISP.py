"""인터페이스의 분리
인터페이스 : 객체가 수신하거나 해석할 수 있는 모든 메세지, 즉, 객체가 노출하는 메서드의 집합

추상 기본 클래스 : 파생 클래스가 반드시 구현해야하는 것을 명시적으로 가리키기 위한 도구
    -> @abstractmethod 사용

핵심은, 여러 메서드를 가진 인터페이스는 명확하게 구분될 수 있는 작은 인터페이스들로 바뀌어야 한다는 것.

앞서 배운 것과 매우 비슷한 흐름을 가지고 있다.
"""
from abc import ABCMeta, abstractmethod


class XMLEventParser(metaclass=ABCMeta):
    @abstractmethod
    def from_xml(xml_data: str):
        """XML Parser"""
        print("xml parser")


class JSONEventParser(metaclass=ABCMeta):
    @abstractmethod
    def from_json(json_data: str):
        """JSON Parser"""
        print("json parser")


class EventParser(XMLEventParser, JSONEventParser):
    """상속받는 각 class에서 @abstractmethod로 지정했기 때문에
    각 메서드에 대해 반드시 구현해야 한다.
    """

    def from_xml(xml_data: str):
        print("xml Parser at EventParser")

    def from_json(json_data: str):
        print("json Parser at EventParser")
