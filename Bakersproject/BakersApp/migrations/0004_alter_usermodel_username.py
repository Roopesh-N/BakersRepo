# Generated by Django 4.2.9 on 2024-03-15 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakersApp', '0003_usermodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='Username',
            field=models.CharField(max_length=30),
        ),
    ]