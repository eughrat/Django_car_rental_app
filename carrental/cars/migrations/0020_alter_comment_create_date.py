# Generated by Django 4.0.3 on 2022-03-14 18:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_alter_comment_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 14, 18, 59, 12, 384561, tzinfo=utc)),
        ),
    ]
