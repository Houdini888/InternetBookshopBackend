# Generated by Django 5.0.1 on 2024-01-21 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0002_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers/'),
        ),
    ]
