# Generated by Django 3.2 on 2023-10-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('erscheinungsjahr', models.CharField(max_length=100)),
                ('verlag', models.CharField(max_length=100)),
            ],
        ),
    ]
