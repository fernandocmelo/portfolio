# Generated by Django 2.0.5 on 2018-08-07 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_socialmedia_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='target',
            field=models.CharField(default='_blank', max_length=15),
        ),
    ]
