# Generated by Django 3.0.3 on 2020-02-20 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page', '0003_auto_20200218_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='reg_agent',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
