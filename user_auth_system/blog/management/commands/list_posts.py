from django.core.management.base import BaseCommand
from blog.models import BlogPost

class Command(BaseCommand):
    help = 'Lists all blog posts and their status'

    def handle(self, *args, **options):
        posts = BlogPost.objects.all()
        if not posts:
            self.stdout.write(self.style.WARNING('No blog posts found in the database.'))
            return

        self.stdout.write(self.style.SUCCESS('Found {} blog posts:'.format(posts.count())))
        for post in posts:
            status = 'DRAFT' if post.is_draft else 'PUBLISHED'
            self.stdout.write(f'- {post.title} (Status: {status}, Author: {post.author.username})') 