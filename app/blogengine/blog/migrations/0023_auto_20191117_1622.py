# Generated by Django 2.2.4 on 2019-11-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20191117_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='media/photos/apple.png', null=True, upload_to='photos/'),
        ),
    ]
