# Generated by Django 4.1.7 on 2023-03-03 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlockPost',
            new_name='BlogPost',
        ),
    ]