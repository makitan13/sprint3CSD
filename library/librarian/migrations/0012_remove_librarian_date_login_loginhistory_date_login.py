# Generated by Django 5.0.6 on 2024-06-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0011_alter_librarian_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='librarian',
            name='date_login',
        ),
        migrations.AddField(
            model_name='loginhistory',
            name='date_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
