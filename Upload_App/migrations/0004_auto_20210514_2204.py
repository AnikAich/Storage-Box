# Generated by Django 2.2.5 on 2021-05-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload_App', '0003_auto_20210508_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploader',
            name='thumbnail',
            field=models.FileField(upload_to='files_storage', verbose_name='File'),
        ),
    ]
