# Generated by Django 4.0.2 on 2022-02-23 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_choice_total_general'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='faculty',
        ),
    ]