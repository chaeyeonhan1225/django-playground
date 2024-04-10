from factory.django import DjangoModelFactory
from factory import Faker

from post.models import Post


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = Faker("text", max_nb_chars=100)
    content = Faker("text", max_nb_chars=200)