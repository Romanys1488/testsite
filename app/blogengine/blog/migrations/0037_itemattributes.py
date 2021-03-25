# Generated by Django 2.2.2 on 2021-01-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_auto_20210128_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ManyToManyField(blank=True, related_name='attributes', to='blog.AttributeType')),
                ('item', models.ManyToManyField(blank=True, related_name='postss', to='blog.Post')),
            ],
        ),
    ]
