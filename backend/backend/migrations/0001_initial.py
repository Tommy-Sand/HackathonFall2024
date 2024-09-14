# Generated by Django 5.1.1 on 2024-09-14 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('resume', models.CharField(max_length=32000000)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_date', models.DateTimeField(verbose_name='date sent')),
                ('status', models.CharField(max_length=200)),
                ('interview_date', models.DateTimeField(verbose_name='date interview')),
                ('accept_date', models.DateTimeField(verbose_name='date accept')),
                ('resume', models.CharField(max_length=32000000)),
                ('job_posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
    ]
