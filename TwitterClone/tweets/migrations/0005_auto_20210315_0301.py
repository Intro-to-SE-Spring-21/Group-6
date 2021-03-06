# Generated by Django 3.1.6 on 2021-03-15 03:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20210315_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='media',
            field=models.ImageField(blank=True, default='testing', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweetID',
            field=models.CharField(default=uuid.UUID('cc40fffb-2d1c-4500-bda3-d9e2345f7573'), max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
