# Generated by Django 5.0.1 on 2024-01-20 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='No description available.', max_length=1000),
        ),
    ]