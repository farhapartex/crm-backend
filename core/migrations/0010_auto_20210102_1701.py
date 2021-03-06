# Generated by Django 3.1.3 on 2021-01-02 17:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_service_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Delete'),
        ),
        migrations.AddField(
            model_name='city',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='country',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Delete'),
        ),
        migrations.AddField(
            model_name='country',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='role',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Delete'),
        ),
        migrations.AddField(
            model_name='role',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='service',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Delete'),
        ),
        migrations.AddField(
            model_name='servicetype',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Delete'),
        ),
        migrations.AddField(
            model_name='servicetype',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Delete'),
        ),
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='verifytoken',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Delete'),
        ),
        migrations.AddField(
            model_name='verifytoken',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
