# Generated by Django 4.1.1 on 2022-10-10 11:12

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='log_color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='log',
            name='log_type',
            field=models.TextField(choices=[('Task Created', 'Task Created'), ('Status Changed', 'Status Changed'), ('Assignee Changed', 'Assignee Changed'), ('Title Changed', 'Title Changed'), ('Description Changed', 'Description Changed')], default='Task Created', max_length=255),
        ),
    ]
