# Generated by Django 3.1.3 on 2021-01-23 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_user_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
    ]
