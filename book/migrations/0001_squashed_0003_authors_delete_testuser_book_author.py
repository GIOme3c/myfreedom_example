# Generated by Django 5.1.5 on 2025-02-06 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('patronymic', models.CharField(blank=True, max_length=30, null=True)),
                ('birthdate', models.DateTimeField()),
                ('deathdate', models.DateTimeField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Биография')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(blank=True, default=100, null=True)),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='book.authors')),
            ],
            options={
                'ordering': ['-published'],
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
