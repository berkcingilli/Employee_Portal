# Generated by Django 3.0 on 2020-04-10 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookleave', '0009_auto_20200410_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='begindate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='leave',
            name='enddate',
            field=models.DateTimeField(),
        ),
    ]
