# Generated by Django 4.2.9 on 2024-03-15 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakersApp', '0002_rename_passsword_usermodel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='Username',
            field=models.CharField(default='NoUname', max_length=30),
        ),
    ]
