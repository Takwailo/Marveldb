# Generated by Django 4.0.4 on 2022-04-27 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abilities', models.CharField(max_length=200)),
                ('real_name', models.CharField(max_length=100)),
            ],
        ),
    ]
