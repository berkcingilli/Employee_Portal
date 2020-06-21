# Generated by Django 3.0 on 2020-03-14 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitystream', '0004_auto_20200310_0029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='document',
            field=models.FileField(blank=True, default=None, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='post',
            name='document',
            field=models.FileField(blank=True, default=None, upload_to='documents'),
        ),
    ]
