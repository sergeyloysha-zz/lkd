# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_title', models.CharField(max_length=250)),
                ('category_slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link_title', models.CharField(max_length=250)),
                ('link_slug', models.SlugField(unique=True, max_length=250)),
                ('link_url', models.URLField()),
                ('link_created', models.DateTimeField(auto_now=True)),
                ('link_category', models.ForeignKey(to='link.Category')),
            ],
            options={
                'verbose_name': '\u0421\u0441\u044b\u043b\u043a\u0430',
                'verbose_name_plural': '\u0421\u0441\u044b\u043b\u043a\u0438',
            },
            bases=(models.Model,),
        ),
    ]
