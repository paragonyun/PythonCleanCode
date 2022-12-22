"""pylint를 통한 LSP 준수 여부 검사
최종적으로 mypy와 pylint 둘 다 사용하는 걸 권장한다.
"""
from LSP_mypy import Event


class LogoutEvent(Event):

    """아예 다른 파라미터를 사용하는 경우 pylint로 탐지할 수 있다."""

    def meets_condition(self, event_data: dict, override: bool) -> bool:
        if override:
            return True


"""
************* Module LSP_pylint
LSP_pylint.py:8:0: C0304: Final newline missing (missing-final-newline)
LSP_pylint.py:1:0: C0103: Module name "LSP_pylint" doesn't conform to snake_case naming style (invalid-name)
LSP_pylint.py:5:0: C0115: Missing class docstring (missing-class-docstring)
LSP_pylint.py:6:4: W0221: Parameters differ from overridden 'meets_condition' method (arguments-differ)
LSP_pylint.py:6:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
LSP_pylint.py:5:0: R0903: Too few public methods (1/2) (too-few-public-methods)

------------------------------------
Your code has been rated at -2.00/10

LSP_pylint.py:6:4: W0221: Parameters differ from overridden 'meets_condition' method (arguments-differ)
"""
