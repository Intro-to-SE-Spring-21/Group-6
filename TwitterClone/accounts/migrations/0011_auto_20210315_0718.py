# Generated by Django 3.1.6 on 2021-03-15 07:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210315_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='userID',
            field=models.CharField(default=uuid.UUID('6201e6dd-e0ba-4dee-819b-9a9e89a8774b'), max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
