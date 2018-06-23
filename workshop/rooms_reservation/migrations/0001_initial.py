# Generated by Django 2.0.3 on 2018-06-23 11:47

from django.db import migrations, models
import django.db.models.deletion


from django.db import migrations, models
import django.db.models.deletion
from rooms_reservation.models import *


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comment', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('capacity', models.IntegerField()),
                ('projector', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms_reservation.Room'),
        ),

    ]

