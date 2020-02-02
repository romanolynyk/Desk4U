# Generated by Django 3.0.2 on 2020-02-01 16:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a Building (e.g. DC)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a University (e.g. University of Waterloo)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.CharField(max_length=200)),
                ('building', models.ManyToManyField(help_text='Select a building for this book', to='availability.Building')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='University',
            field=models.ForeignKey(help_text='Select a university for this building', null=True, on_delete=django.db.models.deletion.SET_NULL, to='availability.University'),
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular desk across whole database', primary_key=True, serialize=False)),
                ('due_back', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Away'), ('o', 'Occupied'), ('a', 'Available')], default='a', help_text='Desk availability', max_length=1)),
                ('desk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='availability.Desk')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
    ]
