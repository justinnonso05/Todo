# Generated by Django 4.2.1 on 2023-06-12 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_todo_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='label',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='todo',
            name='tasks',
            field=models.TextField(),
        ),
    ]
