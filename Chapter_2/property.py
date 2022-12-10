"""
Getter : 데이터를 읽어주는 메서드
Setter : 데이터를 수정하는 메서드
=> 내부 데이터에 대한 접근을 통제하는 역할을 한다.

@property : setter와 getter 메서드의 대상이 될 객체를 지정하는 역할
@x.stter : 유효성 검사를 담당하는 로직

class.x = abc와 같은 방식으로 접근하는 경우 자동으로 @x.setter로 선언된 검사 로직이 자동으로 호출!!

이러한 것은 명령-쿼리 분리 원칙을 준수하는 데에 매우 유용하다.
명령-쿼리 분리 원칙은 하나의 메서드는 setter 기능을 하든지 getter 기능을 하든지 둘 중 하나만 해야한다는 원칙.
단순히 함수 이름으로 이를 지정하기엔 너무 헷갈리므로 
확실하게 perperty 데코레이터로 이를 지정해주는 것!!
"""


class Coordinate:
    def __init__(self, lat: float, long: float) -> None:
        self._latitude = self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if lat_value not in range(-90, 90 + 1):
            raise ValueError(f"유효하지 않은 위도 값입니다. : {lat_value}")
        self._latitude = lat_value

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if long_value not in range(-180, 180 + 1):
            raise ValueError(f"유효하지 않은 위도 값입니다. : {long_value}")
        self._longitude = long_value


coo = Coordinate(10.20, 10.10)
print("처음 값")
print(coo.latitude, coo.longitude)

try:
    coo.longitude = 1000.01  # 에러발생
except:
    coo.longitude = 100.02  # 통과
print("변경 후")
print(coo.latitude, coo.longitude)
