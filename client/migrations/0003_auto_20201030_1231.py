# Generated by Django 3.1.2 on 2020-10-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20201030_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='imp_file',
            field=models.FileField(blank=True, null=True, upload_to='static/Uploads/proposals/'),
        ),
    ]
