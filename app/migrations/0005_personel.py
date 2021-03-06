# Generated by Django 3.1.1 on 2020-09-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200916_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='personel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('specialization', models.CharField(max_length=9)),
                ('hired', models.DateTimeField(auto_now_add=True)),
                ('salary', models.CharField(max_length=8)),
            ],
            options={
                'ordering': ('-hired',),
            },
        ),
    ]
