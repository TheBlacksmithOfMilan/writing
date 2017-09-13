# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-12 07:41
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleUserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'wr_article_user_comment',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 12, 7, 41, 13, 365726, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 12, 7, 41, 13, 366487, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='articleusercomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comment_users', to='article.Article'),
        ),
        migrations.AddField(
            model_name='articleusercomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
