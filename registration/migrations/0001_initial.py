# Generated by Django 3.2 on 2021-04-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Доктор',
                'verbose_name_plural': 'Доктора',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polyclinic', models.CharField(max_length=50)),
                ('doctor', models.CharField(max_length=50)),
                ('visit_time', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('policy_number', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Polyclinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Поликлиника',
                'verbose_name_plural': 'Поликлиники',
                'ordering': ('-name',),
            },
        ),
    ]
