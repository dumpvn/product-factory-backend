# Generated by Django 3.1 on 2021-01-12 11:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0006_auto_20210109_2057'),
        ('work', '0008_auto_20210112_1110'),
        ('matching', '0003_match_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskClaim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('kind', models.IntegerField(choices=[(0, 'NONE'), (1, 'DONE'), (2, 'CLAIMED'), (3, 'FAILED')], default=0)),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent.person')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskClaimRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('task_claim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matching.taskclaim')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]