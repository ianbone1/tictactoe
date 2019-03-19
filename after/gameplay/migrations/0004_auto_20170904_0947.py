# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-09-04 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0003_auto_20170805_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(default=True, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='move',
            name='comment',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='move',
            name='game',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='gameplay.Game'),
        ),
    ]
