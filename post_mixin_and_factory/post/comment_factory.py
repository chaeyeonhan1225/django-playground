from factory.django import DjangoModelFactory
from factory import Faker, SubFactory

from post.models import Comment
from post.post_factory import PostFactory


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    post = SubFactory(PostFactory)
    content = Faker("text", max_nb_chars=200)