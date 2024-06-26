# Generated by Django 5.0.6 on 2024-06-12 23:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('comments', models.TextField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elements.vehicle')),
            ],
        ),
    ]
