# Generated by Django 5.0.6 on 2024-07-12 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0028_alter_librarian_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarian',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
