# Generated by Django 2.0 on 2019-08-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLogFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('path', models.CharField(default='', max_length=1024)),
                ('status', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
