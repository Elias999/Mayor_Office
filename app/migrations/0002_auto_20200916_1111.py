# Generated by Django 3.1.1 on 2020-09-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='made_afm',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='crew',
            name='complains_id',
            field=models.TextField(max_length=330),
        ),
        migrations.AlterField(
            model_name='crew',
            name='crew_members',
            field=models.TextField(max_length=30),
        ),
    ]
