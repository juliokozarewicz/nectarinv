# Generated by Django 5.0.4 on 2024-04-09 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0002_alter_financialinvoices_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financialinvoices',
            name='user',
        ),
    ]
