# Generated by Django 4.1.7 on 2023-03-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255)),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
