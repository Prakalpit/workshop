# Generated by Django 3.2 on 2021-05-03 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0007_alter_homework_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='date',
            field=models.CharField(max_length=12),
        ),
    ]