# Generated by Django 4.2.2 on 2023-06-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_rename_label_id_task_label_rename_user_id_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En progreso'), ('Completada', 'Completada')], max_length=15),
        ),
    ]
