# Generated by Django 4.1.7 on 2023-02-22 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
