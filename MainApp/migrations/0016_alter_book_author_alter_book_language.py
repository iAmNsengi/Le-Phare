# Generated by Django 4.2.6 on 2023-10-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0015_remove_book_publication_year_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]