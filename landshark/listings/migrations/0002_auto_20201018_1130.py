# Generated by Django 3.1 on 2020-10-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='amenity1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='amenity2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='amenity3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='amenity4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='amenity5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='amenity6',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='amenity7',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='amenity8',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
