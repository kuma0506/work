# Generated by Django 3.1.3 on 2020-11-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CountryName_Ja', models.CharField(max_length=255, verbose_name='国名（日本語）')),
                ('CountryName_En', models.CharField(max_length=255, verbose_name='国名（英語）')),
            ],
        ),
    ]
