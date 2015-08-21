# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150820_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='colortag',
            name='parent',
            field=models.ForeignKey(null=True, to='products.ColorTag', blank=True, related_name='sub_colors'),
        ),
    ]
