# Generated by Django 3.1 on 2020-09-30 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0009_auto_20200930_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment_model',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('user_id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from+', to='user.user')),
                ('user_id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to+', to='user.user')),
            ],
        ),
    ]