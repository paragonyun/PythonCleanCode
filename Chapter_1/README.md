# 🚩 Chapter 1 코드 포매팅과 도구
## 📌 알게된 점
> 1. 클린코드는 남이 읽이 좋은 코드다. (프로그래밍은 아이디어의 전달이다.)
> 2. 클린코드는 수정이 용이하게 만들며, 이는 기술부채 방지에 있어 매우 중요하다.
> 3. 표준화된 Layout은 전달력에 있어 매우 큰 도움이 된다.
> 4. PEP8 원칙과 이를 자동화 해주는 도구가 있다. (mypy, black)
> 5. Docstring은 매우 중요하다. 그리고 주석은 줄일 수록 좋다.
> 6. Annotation은 Docstring을 일부 대체할 수 있따. 그러나 Docstring은 엔지니어의 편의상 여전히 유효하다. (@dataset 참고)

<br>

<br>

## 👀 사용 예시
**mypy**  
Type Hint에 맞게 잘 작성 되었는지 확인해주는 도구.  
강제성은 없고, 체크만 해준다. 파이썬의 동적 언어 특징에 의한 단점을 보완해주기 위한 도구!
```CMD
mypy filename.py
```

<br>

**black**  
PEP8을 비롯한 사용자 정의 Format을 준수했는지 검사해주고  
지키지 않았다면 이를 Format에 맞게 바꿔주는 역할을 한다.  
매우 편했음!
```CMD
black filename.py

[체크만 하고 싶을 때]
black --check filename.py
```

