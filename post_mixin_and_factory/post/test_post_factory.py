from django.test import TestCase

from post.post_factory import PostFactory
from post.models import Post


class PostFactoryTest(TestCase):
    def test_build는_instance만_생성(self):
        post = PostFactory.build(title="test")
        self.assertEqual(post.title, "test")
        self.assertIsNone(post.id)

        posts = PostFactory.build_batch(10)
        self.assertEqual(len(posts), 10)

        post_size = Post.objects.all().count()
        self.assertEqual(post_size, 0)  # 실제론 저장 안됨


    def test_create는_create(self):
        post = PostFactory(title="test")
        self.assertEqual(post.title, "test")
        self.assertEqual(post.id, 1)

        posts = PostFactory.create_batch(10)
        self.assertEqual(len(posts), 10)

        post_size = Post.objects.all().count()
        self.assertEqual(post_size, 11)  # 실제로 저장됨

    def test_stub은_단순_데이터(self):
        post = PostFactory.stub(title="stub test")
        self.assertEqual(post.title, "stub test")   # DB에 저장될 수 없는 값

        with self.assertRaises(AttributeError):
            self.assertIsNone(post.id)

