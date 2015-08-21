# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='/statics/'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='parent',
            field=models.ForeignKey(to='products.Tag', null=True, blank=True, related_name='sub_tags'),
        ),
    ]
