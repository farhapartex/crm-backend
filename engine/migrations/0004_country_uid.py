# Generated by Django 3.1.3 on 2021-01-23 17:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_customer_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]