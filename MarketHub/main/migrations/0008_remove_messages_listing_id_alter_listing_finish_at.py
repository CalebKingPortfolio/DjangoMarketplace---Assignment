# Generated by Django 5.0.2 on 2024-03-11 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_listing_finish_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='listing_id',
        ),
        migrations.AlterField(
            model_name='listing',
            name='finish_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 20, 5, 13, 826583, tzinfo=datetime.timezone.utc)),
        ),
    ]
