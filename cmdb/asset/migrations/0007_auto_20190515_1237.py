# Generated by Django 2.2 on 2019-05-15 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0006_auto_20190515_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host_all',
            name='server_number',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='host_all',
            name='server_producter',
            field=models.CharField(default='', max_length=128),
        ),
    ]
