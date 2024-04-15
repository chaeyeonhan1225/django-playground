from post.comment_factory import CommentFactory
from post.models import Post, Comment
from post.post_factory import PostFactory


def create_dummy_posts_and_comments():
    posts = PostFactory.build_batch(size=100)
    Post.objects.bulk_create(posts)
    comments = []
    for post in posts:
        comments.extend(CommentFactory.build_batch(size=20, post=post))

    Comment.objects.bulk_create(comments)



