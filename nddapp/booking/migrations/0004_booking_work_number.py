# Generated by Django 2.0.7 on 2018-07-24 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20180723_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='work_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
