from typing import Iterable, Tuple, Union, List
import logging

logger = logging.getLogger('main')

def broadcast_notification(
    message: str,
    # relevant_user_emails: Iterable[str] # 잘못된 예시 -> 그러나 mypy상으로는 잘못된 게 없으므로 오류를 발생시키지 않는다.
    relevant_user_emails: Union[List[str], Tuple[str]]
):
    for email in relevant_user_emails:
        logger.info(f"{message} 메세지를 {email}에게 전달합니다.")

broadcast_notification("welcome", "user1@domain.com") 

# 사용법 
# cmd에서 mypy [파일이름]