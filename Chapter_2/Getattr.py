"""__getattr__
객체가 속성에 접근하는 방식을 정의할 수 있는 매직 메서드다.
우리가 class.attr로 객체의 속성에 접근할 때 아래의 과정을 거친다.

1. 객체의 속성에 대한 정보를 가지고 있는 __dict__ 에서 해당 속성이 있는지 검색
2-1. 있는 경우 : 해당 속성에 대해 __getattribute__ 메서드 호출
2-2. 없는 경우 : 해당 속성을 파라미터로 하는 __getattr__ 메서드 호출
=> __getattr__을 이용하면 "존재하지 않는 속성을 호출할 때 어떻게 할지"를 정할 수 있게된다.

* 추가 사실
1. __dict__를 이용하면 클래스의 결과로 나오는 인스턴스에 새로운 속성을 "동적"으로 추가할 수 있다.
2. 동적이라는 말은, 같은 클래스로 a와 b 인스턴스를 생성했을 때 a 인스턴스에 동적으로 추가하면 b에는 생기지 않는다는 말

__getattr__의 쓰임새
- 다른 객체에 대한 프록시 역할 
- 중복코드가 많이 발생하거나 보일러플레이트 코드가 많은 경우
- 그러나 막 쓰면 코드의 가독성이 떨어지니 주의! 

"""

## 추가 사실 예시
class DictCase:
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = DictCase(x=1, y=2)
a.z = 3
print(a.z)  # 3

b = DictCase(x=1, y=2)
# print(b.z) # AttributeError: 'DictCase' object has no attribute 'z'


## __getattr__ 예시
class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):  ## 기존에 등록되어 있지 않는 속성(attr)이 들어왔을 때 아래와 같이 처리한다.
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "")
            return f"[fallback resolved] {name}"
        raise AttributeError(f"{self.__class__.__name__}에는 {attr} 속성이 존재하지 않습니다.")


dyn = DynamicAttributes("value")
print(dyn.attribute)  # value, 정상 작동

# fallback_으로 시작하는 새로운 attribute가 들어온 경우
print(dyn.fallback_test)  # [fallback resolved] test

# 아예 새로운 attribute가 들어온 경우
# print(dyn.completely_new_value) # AttributeError: DynamicAttributes에는 completely_new_value 속성이 존재하지 않습니다.

# 새로운 속성을 추가하는 경우
dyn.__dict__["Something_NEW"] = "this is something new attr"
print(dyn.Something_NEW)  # this is something new attr


# getattr 함수는 에러가 발생하는 경우 3번째 인자를 반환한다.
print(getattr(dyn, "somthing", "new"))  # new
