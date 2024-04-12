from django.db import models


class TimeRecordingMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

post_states = (("PUBLISHED", "발행"), ("HIDDEN", "숨김"), ("DELETED", "삭제"))


class Post(TimeRecordingMixin, models.Model):
    title = models.CharField(max_length=40, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    status = models.CharField(
        max_length=20, choices=post_states, blank=False, null=False,
        default="PUBLISHED"
    )

    class Meta:
        db_table = "post"
        ordering = ["-created_at"]


class Comment(TimeRecordingMixin, models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=120, blank=False, null=False)

    class Meta:
        db_table = "comment"
