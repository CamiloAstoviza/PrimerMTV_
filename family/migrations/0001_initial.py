# Generated by Django 4.0.6 on 2022-07-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Lastname', models.CharField(max_length=40)),
                ('Age', models.IntegerField()),
            ],
        ),
    ]
