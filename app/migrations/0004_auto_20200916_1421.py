# Generated by Django 3.1.1 on 2020-09-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200916_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='resolve_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
