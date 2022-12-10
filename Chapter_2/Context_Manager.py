"""
원하는 때에 리소스를 할당하고 제공하기 위한 기능
블록의 전후에 필요로 하는 특정 "로직"을 제공하기 위해 사용될 수 있따.
즉, 독립적인 무언가를 하기 위해 사용!
"""
## 데코레이터 사용 전 코드
def stop_database():
    run("systemctl stop postgresql.service")


def start_database():
    run("systemctl start postgresql.service")


class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()


def db_backup():
    run("pg_dump database")


def main():
    with DBHandler():
        db_backup()


## 데코레이터 사용 후 코드
import contextlib


@contextlib.contextmanager
def db_handler():
    try:
        stop_database()  ## yield 문 앞의 내용들은 모두 __enter__ 메소드의 일부처럼 취급됨
        yield
    finally:  ## yield 문 뒤의 내용들은 모두 __exit__의 로직!
        start_database()


with db_handler():
    db_backup()


## 상속 버전으로 사용하기
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, ext_type, ex_value, ex_traceback):
        start_database


@dbhandler_decorator()
def offline_backup():
    run("pg_dump database")
