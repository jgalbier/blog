# Generated by Django 5.1.6 on 2025-02-05 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='topic',
            new_name='blog',
        ),
    ]
