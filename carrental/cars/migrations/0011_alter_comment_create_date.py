# Generated by Django 4.0.3 on 2022-03-11 21:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_alter_comment_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 21, 33, 6, 221819, tzinfo=utc)),
        ),
    ]
