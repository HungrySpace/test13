# Generated by Django 3.2.9 on 2021-11-13 18:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211113_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesOfQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='surveys',
            name='date_finish',
            field=models.DateField(default=datetime.datetime(2021, 11, 13, 18, 4, 34, 707467, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='surveys',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2021, 11, 13, 18, 4, 34, 707467, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('type', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.typesofquestion')),
            ],
        ),
    ]
