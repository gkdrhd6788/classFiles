# Generated by Django 4.2.5 on 2023-09-15 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0005_book_category_id_book_category_name_book_isbn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Category_id',
        ),
    ]