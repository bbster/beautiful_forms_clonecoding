# Generated by Django 3.1.2 on 2020-10-23 12:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('preferences', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prefernce',
            new_name='Preference',
        ),
    ]
