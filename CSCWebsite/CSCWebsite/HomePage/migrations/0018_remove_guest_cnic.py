# Generated by Django 4.1 on 2024-06-23 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0017_roomtype_room_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='CNIC',
        ),
    ]