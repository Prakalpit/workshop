# Generated by Django 3.2 on 2021-05-03 03:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('url', models.URLField()),
                ('topic', models.CharField(max_length=12)),
                ('date', models.DateField(default=None)),
                ('description_of_homework', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
