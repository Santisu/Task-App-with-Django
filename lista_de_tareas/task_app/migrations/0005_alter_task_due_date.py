# Generated by Django 4.2.2 on 2023-06-30 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0004_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
