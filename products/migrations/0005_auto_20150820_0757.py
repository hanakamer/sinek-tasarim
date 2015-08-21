# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150820_0753'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ColorTags',
            new_name='ColorTag',
        ),
    ]
