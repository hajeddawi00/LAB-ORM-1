# Generated by Django 5.0.3 on 2024-03-18 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Science', 'Science'), ('Culture', 'Culture'), ('Food', 'Food'), ('Tech', 'Tech'), ('Fashion', 'Fashion')], default='General', max_length=20),
        ),
    ]
