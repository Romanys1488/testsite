# Generated by Django 2.2.2 on 2021-02-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0045_auto_20210208_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributetype',
            name='slug',
        ),
        migrations.AddField(
            model_name='attributetype',
            name='slug',
            field=models.ManyToManyField(blank=True, related_name='post_slug', to='blog.Post'),
        ),
    ]
