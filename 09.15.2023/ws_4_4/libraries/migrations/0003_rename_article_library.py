# Generated by Django 4.2.5 on 2023-09-15 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0002_alter_article_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Library',
        ),
    ]