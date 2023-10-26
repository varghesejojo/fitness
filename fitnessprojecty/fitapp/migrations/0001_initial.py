# Generated by Django 4.0.2 on 2023-10-26 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]
