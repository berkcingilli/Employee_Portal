# Generated by Django 3.0 on 2020-04-10 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookleave', '0005_leave_is_rejected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='begindate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='enddate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='type',
            field=models.CharField(choices=[('Sickday', 'SickDay'), ('Vacation', 'Vacation')], max_length=20, verbose_name='Leave Type'),
        ),
    ]
