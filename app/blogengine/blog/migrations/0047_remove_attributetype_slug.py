# Generated by Django 2.2.2 on 2021-02-08 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0046_auto_20210208_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributetype',
            name='slug',
        ),
    ]
