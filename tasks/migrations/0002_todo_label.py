# Generated by Django 4.2.1 on 2023-06-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='label',
            field=models.CharField(default='Add label', max_length=100),
        ),
    ]
