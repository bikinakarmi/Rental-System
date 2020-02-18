# Generated by Django 3.0.3 on 2020-02-18 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_property_property_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='property'),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('H', 'HOUSE'), ('A', 'APARTMENT'), ('S', 'Studion'), ('M', 'Mansion'), ('C', 'COttage')], max_length=1),
        ),
    ]
