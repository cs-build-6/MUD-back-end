# Generated by Django 2.2.5 on 2019-10-22 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20191022_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_db',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
