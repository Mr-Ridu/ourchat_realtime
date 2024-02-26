# Generated by Django 5.0.2 on 2024-02-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='messege_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_user', models.CharField(max_length=250)),
                ('messege', models.TextField()),
                ('m_time', models.DateTimeField(blank=True, null=True)),
                ('m_room', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='room_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=500)),
                ('reffer_code', models.IntegerField()),
                ('username', models.CharField(max_length=250)),
            ],
        ),
    ]
