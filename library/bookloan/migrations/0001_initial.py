# Generated by Django 5.0.6 on 2024-06-26 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('librarian', '0005_remove_bookloan_book_remove_bookloan_member_and_more'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateField()),
                ('due_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.book')),
                ('librarian', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='librarian.librarian')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.member')),
            ],
            options={
                'db_table': 'book_loans',
            },
        ),
    ]
