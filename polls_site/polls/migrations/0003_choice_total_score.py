# Generated by Django 4.0.2 on 2022-02-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_choice_total_ease_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
    ]
