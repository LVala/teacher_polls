# Generated by Django 4.0.2 on 2022-02-22 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_total_score_choice_total_general'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='total_general',
        ),
    ]