# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 07:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171028_0720'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
    ]
