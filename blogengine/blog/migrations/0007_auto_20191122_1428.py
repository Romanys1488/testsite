# Generated by Django 2.2.7 on 2019-11-22 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191122_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='img/index.jpeg', null=True, upload_to='img/'),
        ),
    ]
