# Generated by Django 4.1.3 on 2022-12-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
