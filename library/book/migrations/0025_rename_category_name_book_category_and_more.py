# Generated by Django 5.0.6 on 2024-07-10 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0024_rename_category_book_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category_name',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='category',
        ),
    ]
