# Generated by Django 2.0.1 on 2018-05-12 09:53

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0007_auto_20180511_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='wiki/'),
        ),
    ]