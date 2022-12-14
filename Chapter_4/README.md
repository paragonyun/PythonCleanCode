# π© Chapter 4 SOLID μμΉ
## π μκ²λ μ 
> 1. **SOLID μμΉ**μ νμμ μΈ κ²μ μλμ§λ§ λ―Έλμ μ μ§λ³΄μκ° μννκ² νλ λμμΈ λ°©λ²μ΄λ€.
> 
> 2. **`SRP(λ¨μΌμ±μμμΉ)`** : λͺ¨λ  Classλ νλμ μ±μ(κΈ°λ₯)λ§μ κ°μ§κ³  μμ΄μΌ νλ€.
>       - λλ¬΄ λ§μ μ±μμ λ§μ μμ μ΄ μκ΅¬λλ€.
>       - κΌ­ ClassλΉ κΈ°λ₯μ΄ 1κ°μ¬μΌ νλ€λ κ²μ μλκ³ , Logicμ νμν μ΅μνμ κΈ°λ₯λ§μ κ°μΆμ΄μΌ νλ€λ μλ―Έλ€.
> 3. **`OCP(κ°λ°©νμμ μμΉ)`** : Classλ μΊ‘μνλ LogicμΌλ‘ μ΄λ£¨μ΄μ ΈμΌ νλ©° **μμ μ νμμ μ΄κ³  νμ₯μ κ°λ°©μ μ΄μ΄μΌ νλ€.** 
>       - κΈ°μ‘΄μ κ²μ μμ ν  νμκ° μλλ‘ μ€κ³ν΄μΌ νλ€λ μλ―Έλ€.
> 4. **`LIP(λ¦¬μ€μ½ν μΉν)`** : λΆλͺ¨ Classμ λν΄ λͺ¨λ₯΄κ³  μμ΄λ μ¬μ©μλ λ¬Έμ κ° μμ΄μΌ νλ€.
>       - μ¬λ°λ₯Έ κ³μΈ΅κ΅¬μ‘° μ€κ³μ λν κ²μ΄λ€.
> 5. **`ISP(μΈν°νμ΄μ€ λΆλ¦¬)`** : SRPμ λΉμ·νκ² μΈν°νμ΄μ€μ κΈ°λ₯μ λΆλ¦¬ν΄μΌ νλ€λ μλ―Έμ΄λ€.
>       - μμ μΈν°νμ΄μ€λ₯Ό μ§ν₯νλ€.
> 6. **`DIP(μμ‘΄μ± μ­μ )`** : μ½λλ λ€λ₯Έ μ½λμ λλ¬΄ κ³Όνκ² μμ‘΄ν΄μ  μ λλ€. 
>       - ν΅μ¬μ ν μ½λ λ΄μμ νμν κΈ°λ₯μ΄λ μμλ₯Ό μμ±νλ κ²μ΄ μλ, μ κ³΅μ λ°μλ κ²μ΄λ€.


<br>

<br>

## π μ¬μ© μμ

**OCP** (κ°μΈμ μΌλ‘ κ°μ₯ κΈ°λ°νλ€κ³  μκ°νλ€.)
```python
class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False


class UnkownEvent(Event):
    """μκΉμ κ°μ μν©μΌ λ"""


class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
            event_data["before"]["session"] == 0
            and event_data["before"]["session"] == 1
        )


class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
            event_data["before"]["session"] == 1
            and event_data["before"]["session"] == 0
        )


class SystemMonitor:
    """μ¬κΈ°μ λΆλ₯"""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):  ## μ΄κ² Trueλ₯Ό λ°ννλ©΄
                    return event_cls(self.event_data)  ## ν΄λΉ μ‘°κ±΄ λ°ν

            except KeyError:
                continue

        return UnkownEvent(self.event_data)
```

<br>

**DIP**
```python
class EventStreamer:
    """μμ‘΄μ± μ£Όμ μ 
    λ¨μ νμ€νΈλ₯Ό ν  λλ Syslogλ₯Ό μμ ν΄μΌ νκ³  λ§μ½ syslogμ λ¬Έμ κ° μλ€λ©΄ 
    κ·Έ λ¬Έμ κ° μ΄κΈ°ν ν  λ κ·Έλλ‘ λ°μν¨
    (μ μ΄μ init μμ λ¬΄μΈκ°λ₯Ό μμ±νλ κ²μ κΆμ₯νμ§λ μμ)
    """
    def __init__(self):
        self._target = Syslog()

    def stream(self, events: list[Event]) -> None:
        for event in events:
            self._target.send(event.serialise())

class EventStreamer:
    """μμ‘΄μ± μ£Όμ ν
    μ§μ  κ΄λ¦¬νλ κ²μ΄ μλ νμν μ λ³΄λ₯Ό μ κ³΅λ°λ κ²
    
    μ΄λ κ² νλ©΄ μ΄κΈ°ν μ λ€μν κ°μ²΄ μ λ¬μ΄ κ°λ₯νκ³  νμ€νΈλ λ κ°λ¨ν΄μ‘μ
    """
    def __init__(self, target: DataTargetClient):
        self._target = target

    def stream(self, events: list[Event]) -> None:
        for event in events:
            self._target.send(event.serialise())
```