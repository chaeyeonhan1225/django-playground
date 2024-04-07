from django.db import models

post_states = (("PUBLISHED", "발행"), ("HIDDEN", "숨김"), ("DELETED", "삭제"))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    status = models.CharField(
        max_length=20, choices=post_states, blank=False, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "post"
        ordering = ["-created_at"]
