# Generated by Django 2.2 on 2019-04-04 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='age3',
            new_name='age',
        ),
        migrations.RemoveField(
            model_name='person',
            name='age1',
        ),
        migrations.RemoveField(
            model_name='person',
            name='age2',
        ),
    ]