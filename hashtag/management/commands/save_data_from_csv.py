from django.core.management.base import BaseCommand
from hashtag.models import SocialMediaPost
import csv

class Command(BaseCommand):
    help = 'Import test data from CSV file'

    def handle(self, *args, **kwargs):
        csv_file_path = ''#path of your csv file

        with open(csv_file_path, 'r' ,encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                SocialMediaPost.objects.create(
                    dateTime=row['DateTime'],
                    content=row['PostContent'],
                    clicks=row['Clicks']
                )

        self.stdout.write(self.style.SUCCESS('Test data imported successfully'))
