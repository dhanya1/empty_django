# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='amount',
        ),
        migrations.AddField(
            model_name='item',
            name='county',
            field=models.CharField(max_length=30, default='Unknown'),
            preserve_default=False,
        ),
    ]
