# Generated by Django 5.1.3 on 2024-12-04 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FloexrtaDecorapp', '0003_imagemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='price',
        ),
    ]
