# Generated by Django 3.0 on 2020-03-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitystream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='document',
            field=models.FileField(default=None, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(default=None, upload_to='documents'),
        ),
    ]
