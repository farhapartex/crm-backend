# Generated by Django 3.1.3 on 2021-01-03 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
