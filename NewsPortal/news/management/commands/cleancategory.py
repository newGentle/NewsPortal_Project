from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category
 
 
class Command(BaseCommand):
    help = 'Подсказка вашей команды' # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    requires_migrations_checks = True # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)
    
    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        self.stdout.write(f'Do you reaaly want to delete {options["category"]}? yes/no')
        answer = input()
        _categories = Category.objects.get(category_name=options['category'])
        self.stdout.write(f'{_categories.id}')
        if answer == 'yes': # в случае подтверждения действительно удаляем все товары
            try:
                Post.objects.filter(categories=_categories).delete()
                self.stdout.write(self.style.SUCCESS(f'ALL Posts in category {_categories.category_name} successfully deleted'))

            except _categories.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Wrong Args'))
 