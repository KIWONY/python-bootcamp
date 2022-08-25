```python
class ClassName:
    def __init__(self):

```

`__init__함수`

- 속성을 초기화하는 데에 사용.
- 이 init 함수 안에서 속성을 초기화하거나 시작값을 지정.
- 이 클래스에서 새로운 객체를 만들 때마다 init 함수가 호출됨

<br/>

<hr>

<br/>

아래와 같이 class를 정의하고 객체를 생성한다치면  
속성이 많거나 새로운 객체를 생성할 때마다 아래 순서를 반복해야함

```python
class User:
    pass

user_id = User()
# 속성 추가
user_1.id = "1"
user_1.name = "apple"

```

이를 방지하기 위해 객체를 초기화 하는 **init**함수를 사용한다.

```python
class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0  # 기본값
```

- self는 만들어지고 있는, 또는 초기화되고 있는 실제 객체이다.
- **init**함수에서 객체의 속성값을 설정한다.
- 위에서 user_1의 객체를 생성하는 방식은 init함수를 사용하면 아래의 코드로 바꿀 수 있다. 같다.

```python
user_1 = User(1, apple)
```
