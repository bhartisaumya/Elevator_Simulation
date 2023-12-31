# Generated by Django 4.2 on 2023-05-01 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('current_floor', models.IntegerField(default=0)),
                ('is_operational', models.BooleanField(default=True)),
                ('is_moving', models.BooleanField(default=True)),
                ('direction', models.IntegerField(null=True)),
                ('door_opened', models.BooleanField(default=False)),
                ('last_floor', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElevatorRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('elevator_current_floor', models.IntegerField(null=True)),
                ('target_floor', models.IntegerField(null=True)),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('elevator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elevator', to='elevator_apis.elevator')),
            ],
        ),
    ]
