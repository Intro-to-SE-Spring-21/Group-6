# Generated by Django 3.1.6 on 2021-03-15 02:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='userID',
            field=models.CharField(default=uuid.UUID('ca100566-f608-4bd9-ac27-6f3229a2849b'), max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
