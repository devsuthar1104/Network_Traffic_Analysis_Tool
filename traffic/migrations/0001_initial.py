# Generated by Django 5.0.6 on 2024-05-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrafficData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('source_ip', models.CharField(max_length=45)),
                ('dest_ip', models.CharField(max_length=45)),
                ('protocol', models.CharField(max_length=10)),
                ('length', models.IntegerField()),
                ('info', models.TextField()),
            ],
        ),
    ]
