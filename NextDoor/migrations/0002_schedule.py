# Generated by Django 2.1.2 on 2018-11-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NextDoor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
            ],
        ),
    ]
