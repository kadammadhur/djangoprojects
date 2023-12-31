# Generated by Django 3.2.18 on 2023-09-02 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=40)),
                ('dob', models.DateField()),
            ],
        ),
    ]
