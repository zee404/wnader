# Generated by Django 3.2.18 on 2023-05-15 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wnader', '0026_auto_20230515_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amenities',
            name='category',
        ),
    ]
