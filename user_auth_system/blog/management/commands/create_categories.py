from django.core.management.base import BaseCommand
from blog.models import Category
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Creates initial blog categories'

    def handle(self, *args, **kwargs):
        categories = [
            'Mental Health',
            'Heart Disease',
            'Covid19',
            'Immunization'
        ]

        for category_name in categories:
            slug = slugify(category_name)
            Category.objects.get_or_create(
                name=category_name,
                slug=slug
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created category "{category_name}"')
            ) 