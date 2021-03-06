# Generated by Django 2.0.7 on 2018-07-23 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('address', models.CharField(blank=True, default='', max_length=200)),
                ('principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shippers', to='customer.Principal')),
            ],
        ),
    ]
