# management/commands/populate_db.py
import os
import csv
from django.core.management.base import BaseCommand
from accounts.models import CustomUser
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the database with data from a CSV file'

    def handle(self, *args, **options):
        # Get the directory of the current file (populate_db.py)
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the full path to your CSV file
        file_path = os.path.join(current_directory, 'temp.csv')  # Replace 'file.csv' with your actual CSV file name

        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                date_str = row['date_joined']
                formatted_date = datetime.strptime(date_str, '%m/%d/%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S')
                row['date_joined'] = formatted_date

                CustomUser.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
