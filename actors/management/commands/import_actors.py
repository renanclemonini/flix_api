import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com atores',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            qtd = 0
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d')
                nationality = row['nationality']
                verify = Actor.objects.all().filter(name=name).first()
                if verify is None:
                    # print(verify)
                # print(f'{name} - {birthday} - {nationality}')
                    Actor.objects.create(
                        name=name,
                        birthday=birthday,
                        nationality=nationality
                    )
                    qtd += 1
        self.stdout.write(self.style.SUCCESS(f'{qtd} Atores Importados com Sucesso!'))