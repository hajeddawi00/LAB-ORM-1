# Generated by Django 5.0.3 on 2024-03-18 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
