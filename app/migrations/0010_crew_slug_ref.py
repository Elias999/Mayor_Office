# Generated by Django 3.1.1 on 2020-09-19 19:02

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200919_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='crew',
            name='slug_ref',
            field=autoslug.fields.AutoSlugField(default=12, editable=False, populate_from='UUID'),
            preserve_default=False,
        ),
    ]
