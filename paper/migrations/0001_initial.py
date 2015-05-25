# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_title', models.CharField(max_length=250, db_index=True)),
                ('category_slug', models.SlugField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField()),
                ('comment_created', models.DateTimeField(auto_now=True)),
                ('comment_author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paper_title', models.CharField(unique=True, max_length=250)),
                ('paper_slug', models.SlugField(unique=True, max_length=250)),
                ('paper_text', models.TextField()),
                ('paper_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('paper_updated', models.DateTimeField(auto_now=True)),
                ('paper_author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('paper_category', models.ForeignKey(to='paper.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_paper',
            field=models.ForeignKey(to='paper.Paper'),
            preserve_default=True,
        ),
    ]
