# Generated by Django 3.1.1 on 2020-09-08 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_auto_20200905_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('count_day', models.IntegerField()),
                ('count_internet', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]