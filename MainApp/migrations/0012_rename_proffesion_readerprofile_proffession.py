# Generated by Django 4.2.6 on 2023-10-25 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0011_rename_news_newsandevents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readerprofile',
            old_name='proffesion',
            new_name='proffession',
        ),
    ]