# Generated by Django 3.0.2 on 2020-02-01 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('availability', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookInstance',
            new_name='DeskInstance',
        ),
    ]
