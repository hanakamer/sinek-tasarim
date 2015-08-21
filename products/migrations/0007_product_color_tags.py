# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_colortag_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color_tags',
            field=models.ManyToManyField(related_name='products_of_color', to='products.ColorTag'),
        ),
    ]
