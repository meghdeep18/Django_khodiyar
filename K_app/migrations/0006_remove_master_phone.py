# Generated by Django 5.1 on 2024-11-14 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('K_app', '0005_rename_name_master_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='phone',
        ),
    ]