# Generated by Django 4.0.4 on 2022-05-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_delete_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('program_id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('program_name', models.CharField(max_length=200)),
            ],
        ),
    ]
