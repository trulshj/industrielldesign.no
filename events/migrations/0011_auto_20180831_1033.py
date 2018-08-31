# Generated by Django 2.0.1 on 2018-08-31 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_event_registration_year_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='registration_year_limit',
            field=models.IntegerField(blank=True, choices=[(2023, '1.klasse'), (2022, '2.klasse'), (2021, '3.klasse'), (2020, '4.klasse'), (2019, '5.klasse')], null=True, verbose_name='Åpent for n.klasse og opp'),
        ),
    ]
