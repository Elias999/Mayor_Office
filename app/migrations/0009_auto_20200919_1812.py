# Generated by Django 3.1.1 on 2020-09-19 18:12

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200919_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='slug_ref',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='slug'),
        ),
    ]
