# Generated by Django 5.0.4 on 2024-04-09 14:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialinvoices',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
