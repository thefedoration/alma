# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
