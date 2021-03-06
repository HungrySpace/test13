# Generated by Django 3.2.9 on 2021-11-13 18:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211113_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='survey',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='api.surveys'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='surveys',
            name='date_finish',
            field=models.DateField(default=datetime.datetime(2021, 11, 13, 18, 11, 11, 43181, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='surveys',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2021, 11, 13, 18, 11, 11, 43181, tzinfo=utc)),
        ),
    ]
