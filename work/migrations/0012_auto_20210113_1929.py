# Generated by Django 3.1 on 2021-01-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0011_auto_20210113_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='depend_on',
            field=models.ManyToManyField(related_name='_task_depend_on_+', to='work.Task'),
        ),
    ]