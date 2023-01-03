"""데코레이터에 파라미터를 넣고 싶은 경우
파라미터를 넣기 위해선 간접 참조가 필요하다 (간접 참조 : a=1, b=a c=b -> c=1 이런 식으로 간접적으로 참조하는 것)

1. 파라미터를 받아서 내부 함수에 전달하는 함수
2. 데코레이터가 될 함수
3. 데코레이팅의 결과를 반환하는 함수

@retry(arg1, arg2..) 는 아래와 같다.
<ori_function> = retry(arg1, arg2..)(<ori_function>)
"""
_DEFAULT_RETRIES_LIMIT = 3

def with_retry(
    retries_limit: int = _DEFAULT_RETRIES_LIMIT,
    allowed_exceptions: Optional[Sequence[Exception]] = None,
):
    allowed_exceptions allowed_exceptions or (ControlledException,)

    def retry(operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None
            for _ in range(retries_limit):
                try:
                    return operation(*args, **kwargs)

                except allowed_exceptions as e:
                    logger.warning(
                        f"{operation.__qualname__} 재시도, 원인: {e}"
                    )
                    last_raised = e
                raise last_raised
            
            return wrapped
        
        return retry

@with_retry()
def run_operation(task):
    return task.run()

@with_retry(retries_limit=5)
def run_with_custom_retries_limit(task):
    return task.run()

@with_retry(allowed_exceptions=(AttributeError,))
def run_with_custom_exceptions(task):
    return task.run()

@with_retry(
    retries_limit=4, allowed_exceptions=(ZeroDivisionError, AttributeError)
)
def run_with_custom_parameters(task):
    return task.run()

"""위와 같이 함수를 막 중첩해나가면서 Decorator를 생성할 수 있긴 하지만 너무 알아보기가 어려움"""

##############################################################################################

"""
그러나 이렇게 class로 만들고 __call__ 함수에 해당 기능을 넣어주면 더 깔끔하게 표현 가능함

수행 순서
1. 파라미터를 사용해 Decorator 객체 생성
2. Decorator 객체는 __init__에 정해져 있는 초기화 진행
3. @ 연산 호출
4. Decorator 객체가 해당 함수를 Wrapping 하여 __call__안에 있는 것을 진행
5. __call__은 원본 함수를 래핑하여 새로운 로직이 적용된 함수를 반환
"""
_DEFAULT_RETRIES_LIMIT = 3
class WithRetry:
    def __init__(
        self, 
        retries_limit: int = _DEFAULT_RETRIES_LIMIT,
        allowed_exceptions: Optional[Sequence[Exception]] = None,
    ) -> None:
        self.retries_limit = retries_limit
        self.allowed_exceptions = allowed_exceptions or (ControlledException,)
    
    def __call__(self, operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None
            for _ in range(self.retries_limit):
                try:
                    return operation(*args, **kwargs)

                except self.allowed_exceptions as e:
                    logger.warning(
                        f"{operation.__qualname__} 재시도, 원인: {e}"
                    )
                    last_raised = e
                raise last_raised
        return wrapped

@WithRetry(retries_limit=5)
def run_with_custom_retries_limit_class(task):
    return task.run()
