# Generated by Django 4.0.2 on 2022-02-27 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmain',
            old_name='make',
            new_name='marka',
        ),
    ]
