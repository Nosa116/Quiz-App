# Generated by Django 5.1.1 on 2024-11-22 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='questions',
            new_name='question',
        ),
    ]
