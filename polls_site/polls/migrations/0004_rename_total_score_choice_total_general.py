# Generated by Django 4.0.2 on 2022-02-21 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice_total_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='total_score',
            new_name='total_general',
        ),
    ]