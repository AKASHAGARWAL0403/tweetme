# Generated by Django 2.2.2 on 2019-06-10 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='isReply',
            field=models.BooleanField(default=False, verbose_name='Is a reply?'),
        ),
    ]