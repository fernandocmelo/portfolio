# Generated by Django 2.0.5 on 2018-08-08 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_auto_20180807_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldescription',
            name='active',
            field=models.CharField(default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='personaldescription',
            name='checked',
            field=models.CharField(default='checked', max_length=10),
        ),
    ]
