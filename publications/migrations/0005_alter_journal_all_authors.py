# Generated by Django 4.2.8 on 2023-12-19 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_journal_all_authors_journal_extras_journal_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='all_authors',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]