# Generated by Django 5.1.3 on 2024-11-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FloexrtaDecorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('design_type', models.CharField(max_length=50)),
                ('budget', models.CharField(max_length=50)),
                ('color_preference', models.CharField(max_length=50)),
                ('furniture_needs', models.CharField(max_length=50)),
                ('flooring_preference', models.CharField(max_length=50)),
                ('timeline', models.CharField(max_length=50)),
                ('comments', models.TextField()),
            ],
        ),
    ]
