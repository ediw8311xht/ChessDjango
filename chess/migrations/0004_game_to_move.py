# Generated by Django 4.1.9 on 2023-07-06 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0003_alter_game_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='to_move',
            field=models.CharField(default='white', max_length=5),
        ),
    ]