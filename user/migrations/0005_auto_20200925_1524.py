# Generated by Django 3.1 on 2020-09-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200925_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='authoritystatus',
            field=models.IntegerField(default=0),
        ),
    ]
