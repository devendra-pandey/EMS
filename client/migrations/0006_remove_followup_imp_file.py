# Generated by Django 3.1.2 on 2020-10-30 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20201030_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followup',
            name='imp_file',
        ),
    ]