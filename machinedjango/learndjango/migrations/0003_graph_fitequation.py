# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learndjango', '0002_remove_graph_fitequation'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='fitequation',
            field=models.BinaryField(null=True),
        ),
    ]
