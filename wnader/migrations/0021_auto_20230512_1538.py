# Generated by Django 3.2.18 on 2023-05-12 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wnader', '0020_auto_20230512_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planattraction',
            name='plan',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wnader.customerplan'),
        ),
        migrations.AlterField(
            model_name='planrestaurant',
            name='plan',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wnader.customerplan'),
        ),
    ]
