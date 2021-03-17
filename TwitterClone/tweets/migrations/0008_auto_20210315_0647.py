# Generated by Django 3.1.6 on 2021-03-15 06:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_auto_20210315_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweetID',
            field=models.CharField(default=uuid.UUID('c83b9347-a1c0-4f59-bf8c-26085ad96022'), max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]