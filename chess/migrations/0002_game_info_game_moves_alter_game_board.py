# Generated by Django 4.1.9 on 2023-07-05 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='info',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='moves',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='board',
            field=models.CharField(max_length=100),
        ),
    ]
