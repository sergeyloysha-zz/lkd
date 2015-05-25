# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_link_link_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link_slug',
            field=models.SlugField(max_length=250),
            preserve_default=True,
        ),
    ]
