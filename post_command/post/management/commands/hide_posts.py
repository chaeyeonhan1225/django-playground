from django.core.management.base import BaseCommand, CommandError
from post.models import Post


class Command(BaseCommand):
    help = "hide posts"

    def add_arguments(self, parser):
        parser.add_argument("post_ids", nargs="+", type=int)
        parser.add_argument("--exclude_deleted", action="store_true", default=False)

    def handle(self, *args, **options):
        posts = Post.objects.filter(id__in=options["post_ids"])
        for post in posts:
            if options["exclude_deleted"] and post.status == "DELETED":
                raise CommandError("삭제된 게시글이 존재합니다.")
            post.status = "HIDDEN"

        Post.objects.bulk_update(posts, ["status"])

        self.stdout.write("hide %d posts" % posts.count())
