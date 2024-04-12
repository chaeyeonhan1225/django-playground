# post_mixin_and_factory
## Mixin
- 추상 model을 만들어 중복되는 코드를 없앤다.
```python
class TimeRecordingMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```
## Factory
- factory_boy 설치
- Factory로 인스턴스 생성, faker로 임의의 테스트 값 지정 가능
```python
class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = Faker("text", max_nb_chars=100)
    content = Faker("text", max_nb_chars=200)
```