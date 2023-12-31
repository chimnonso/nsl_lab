# Generated by Django 4.2.8 on 2023-12-21 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publications', '0005_alter_journal_all_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='journals/'),
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('conference_name', models.CharField(max_length=500, null=True)),
                ('abstract', models.TextField(null=True)),
                ('status', models.IntegerField(choices=[(1, 'Preparation'), (2, 'Submitted'), (3, 'Under Review'), (4, 'Accepted'), (5, 'Best Paper'), (6, 'Minor Revision'), (7, 'Rejected')], default=1)),
                ('write_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('visit', models.IntegerField(default=1)),
                ('ack', models.CharField(blank=True, max_length=100, null=True)),
                ('pub_year', models.CharField(blank=True, max_length=10)),
                ('extras', models.CharField(blank=True, max_length=50, null=True)),
                ('all_authors', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='conference/')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='conference', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
