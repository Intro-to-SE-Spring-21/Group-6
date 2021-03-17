# Generated by Django 3.1.6 on 2021-03-15 06:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210315_0643'),
        ('tweets', '0006_auto_20210315_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweetID',
            field=models.CharField(default=uuid.UUID('bf159b0b-a482-43d4-b27a-f86b59451588'), max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='likeTweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.tweet')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]