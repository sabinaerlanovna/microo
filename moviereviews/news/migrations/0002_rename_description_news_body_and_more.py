# Generated by Django 5.0.6 on 2024-06-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='description',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='headline',
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(),
        ),
    ]