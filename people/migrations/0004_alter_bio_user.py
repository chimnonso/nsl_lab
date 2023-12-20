# Generated by Django 4.2.8 on 2023-12-19 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0003_remove_bio_positions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bio', to=settings.AUTH_USER_MODEL),
        ),
    ]
