# Generated by Django 3.1.2 on 2020-10-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikrotik', '0002_auto_20201002_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metricmikrotik',
            name='traff_download',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='metricmikrotik',
            name='traff_uploads',
            field=models.IntegerField(),
        ),
    ]
