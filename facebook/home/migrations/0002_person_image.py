# Generated by Django 3.1.5 on 2021-01-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(default='', upload_to='home'),
        ),
    ]
