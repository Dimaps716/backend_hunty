# Generated by Django 3.1.4 on 2021-12-17 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('CompanyId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Link', models.URLField(blank=True, null=True)),
                ('Country', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('DateAdded', models.DateField()),
                ('ContactFirstName', models.CharField(max_length=100)),
                ('ContactLastName', models.CharField(max_length=100)),
                ('ContactPhoneNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('ContactEmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('VacancyId', models.AutoField(primary_key=True, serialize=False)),
                ('PositionName', models.CharField(max_length=100)),
                ('VacancyLink', models.URLField(blank=True)),
                ('Salary', models.IntegerField()),
                ('Skills', models.TextField(blank=True, null=True)),
                ('MaxExperience', models.IntegerField()),
                ('MinExperience', models.IntegerField()),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('FINALIZE', 'FINALIZE')], default='ACTIVE', max_length=15)),
                ('CompanyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.company')),
            ],
        ),
    ]
