# Generated by Django 2.2.2 on 2021-02-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_auto_20210201_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='hyperlink',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='hyperlinkText',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
