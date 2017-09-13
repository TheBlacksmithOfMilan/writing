# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-24 10:58
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('intro', models.TextField(blank=True)),
                ('status', models.CharField(max_length=16)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 8, 24, 10, 58, 1, 927511, tzinfo=utc))),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'wr_article',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_number', models.IntegerField()),
                ('body', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article')),
            ],
            options={
                'db_table': 'wr_article_comment',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=16)),
                ('body', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('status', models.CharField(max_length=16)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 8, 24, 10, 58, 1, 928402, tzinfo=utc))),
                ('updated', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='article.Article')),
            ],
            options={
                'db_table': 'wr_article_post',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='article_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_post_comments', to='article.ArticlePost'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]