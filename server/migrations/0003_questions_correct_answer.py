# Generated by Django 5.1.1 on 2024-11-22 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_rename_questions_questions_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='correct_answer',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
