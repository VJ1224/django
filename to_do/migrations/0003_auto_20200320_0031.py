# Generated by Django 3.0.4 on 2020-03-19 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0002_todoitem_done'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={'ordering': ['done', 'date_due', 'category']},
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='date_create',
            field=models.DateField(default=datetime.date(2020, 3, 19)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='description',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
