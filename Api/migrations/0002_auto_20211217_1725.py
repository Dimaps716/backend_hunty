# Generated by Django 3.1.4 on 2021-12-17 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='VacancyLink',
            field=models.URLField(blank=True, null=True),
        ),
    ]