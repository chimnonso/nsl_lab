import os
import csv
from django.core.management.base import BaseCommand
from publications.models import Journal
from django.utils import timezone
from datetime import datetime

# DEFAULT_DATE = datetime(1970, 12, 1, 00, 00, 0)

class Command(BaseCommand):
    help = 'Populate the database with data from a CSV file'

    def handle(self, *args, **options):
        # Get the directory of the current file (populate_db.py)
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the full path to your CSV file
        file_path = os.path.join(current_directory, 'journals.csv')  # Replace 'file.csv' with your actual CSV file name

        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:

                
                    
                write_date_str = row['write_date']
                update_date_str = row['update_date']

                formatted_write_date = datetime.strptime(write_date_str, '%m/%d/%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S')
                formatted_update_date = datetime.strptime(update_date_str, '%m/%d/%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S')

                row['write_date'] = formatted_write_date
                row['update_date'] = formatted_update_date
                

                Journal.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
