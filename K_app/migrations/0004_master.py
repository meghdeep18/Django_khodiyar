# Generated by Django 5.1 on 2024-09-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('K_app', '0003_remove_blogpost_category_remove_blogpost_tags_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]