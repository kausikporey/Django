# Generated by Django 3.1.5 on 2021-01-28 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210127_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
    ]
