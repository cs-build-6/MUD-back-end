# Generated by Django 2.2.5 on 2019-10-22 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_personalnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room_DB',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('coords', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('n_to', models.CharField(max_length=20)),
                ('s_to', models.CharField(max_length=20)),
                ('e_to', models.CharField(max_length=20)),
                ('w_to', models.CharField(max_length=20)),
                ('u_to', models.CharField(max_length=20)),
                ('d_to', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
