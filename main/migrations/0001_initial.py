# Generated by Django 4.0.4 on 2022-05-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseId', models.UUIDField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('eligibility', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Syllabus', models.TextField(blank=True, null=True)),
                ('Program_objective', models.TextField(blank=True, null=True)),
                ('Course_objective', models.TextField(blank=True, null=True)),
                ('fees', models.CharField(max_length=200)),
                ('apply_now', models.CharField(max_length=200)),
            ],
        ),
    ]
