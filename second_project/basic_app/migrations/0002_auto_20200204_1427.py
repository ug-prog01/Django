# Generated by Django 3.0.2 on 2020-02-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
