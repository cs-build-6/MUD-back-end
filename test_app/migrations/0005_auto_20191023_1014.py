# Generated by Django 2.2.5 on 2019-10-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_auto_20191022_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_db',
            name='item_owner',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item_db',
            name='item_room',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item_db',
            name='noun',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='item_db',
            name='skill',
            field=models.CharField(max_length=50),
        ),
    ]
