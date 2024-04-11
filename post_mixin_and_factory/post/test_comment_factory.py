from django.test import TestCase

from post.comment_factory import CommentFactory
from post.post_factory import PostFactory
from post.models import Post


class CommentFactoryTest(TestCase):
    def test_comment를_create(self):
        comment = CommentFactory(content="test")
        self.assertEqual(comment.content, "test")
        self.assertEqual(comment.id, 1)

        self.assertIsNotNone(comment.post)
        self.assertEqual(comment.post.id, 1)

        post = Post.objects.get(id=comment.post.id)
        self.assertIsNotNone(post.comments)
        self.assertEqual(post.comments.count(), 1)

    def test_comment를_create_batch(self):
        comments = CommentFactory.create_batch(size=10)
        comment_post = comments[0].post

        self.assertNotEquals(len(comments), comment_post.comments.count())

        post = PostFactory()
        post_comments = CommentFactory.create_batch(size=10, post=post)

        self.assertEqual(len(post_comments), post.comments.count())

