# Generated by Django 3.1.6 on 2021-03-15 03:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210315_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='userID',
            field=models.CharField(default=uuid.UUID('d85fbcce-5f64-4866-9c19-ea62438f0fe0'), max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
