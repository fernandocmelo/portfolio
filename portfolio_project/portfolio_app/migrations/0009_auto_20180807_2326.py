# Generated by Django 2.0.5 on 2018-08-08 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0008_auto_20180807_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldescription',
            name='active',
        ),
        migrations.RemoveField(
            model_name='personaldescription',
            name='checked',
        ),
    ]
