# Generated by Django 5.0.6 on 2024-07-10 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0023_rename_category_category_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category',
            new_name='category_name',
        ),
    ]
