# Generated by Django 3.2.18 on 2023-04-04 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wnader', '0004_auto_20230404_1128'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attraction',
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Attraction', 'verbose_name_plural': 'Attractions'},
        ),
    ]
