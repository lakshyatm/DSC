# Generated by Django 3.0.6 on 2020-09-18 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0007_kitty_person3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitty',
            name='person3',
        ),
    ]