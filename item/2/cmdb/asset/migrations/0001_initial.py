# Generated by Django 2.0 on 2019-08-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('ip', models.GenericIPAddressField(default='0.0.0.0')),
                ('mac', models.CharField(default='', max_length=32)),
                ('os', models.CharField(default='', max_length=64)),
                ('arch', models.CharField(default='', max_length=16)),
                ('mem', models.BigIntegerField(default=0)),
                ('cpu', models.IntegerField(default=0)),
                ('disk', models.CharField(default='{}', max_length=512)),
                ('sn', models.CharField(default='', max_length=128)),
                ('user', models.CharField(default='', max_length=128)),
                ('remark', models.TextField(default='')),
                ('purchase_time', models.DateTimeField()),
                ('over_insurance_time', models.DateTimeField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_time', models.DateTimeField()),
            ],
        ),
    ]