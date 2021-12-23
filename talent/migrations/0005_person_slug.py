# Generated by Django 3.1 on 2021-01-07 17:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0004_auto_20210106_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2021, 1, 7, 17, 47, 5, 794688, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]