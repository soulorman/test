# Generated by Django 2.2 on 2019-05-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0008_monitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='auth',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='celery',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='config',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='insights',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='mysql',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='nginx',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='path',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='redis',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='registry',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='save_log',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='tensorflow_model_server',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='thoslide',
        ),
        migrations.AddField(
            model_name='monitor',
            name='cpu',
            field=models.CharField(default='{}', max_length=512),
        ),
        migrations.AddField(
            model_name='monitor',
            name='isalive',
            field=models.CharField(default='{}', max_length=512),
        ),
        migrations.AddField(
            model_name='monitor',
            name='mem',
            field=models.CharField(default='{}', max_length=512),
        ),
    ]