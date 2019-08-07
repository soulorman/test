# Generated by Django 2.2 on 2019-05-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0007_auto_20190515_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(default='0.0.0.0')),
                ('auth', models.CharField(default='', max_length=128)),
                ('path', models.CharField(default='', max_length=128)),
                ('insights', models.CharField(default='', max_length=128)),
                ('thoslide', models.CharField(default='', max_length=128)),
                ('config', models.CharField(default='', max_length=128)),
                ('registry', models.CharField(default='', max_length=128)),
                ('tensorflow_model_server', models.CharField(default='', max_length=128)),
                ('save_log', models.CharField(default='', max_length=128)),
                ('celery', models.CharField(default='', max_length=128)),
                ('redis', models.CharField(default='', max_length=128)),
                ('nginx', models.CharField(default='', max_length=128)),
                ('mysql', models.CharField(default='', max_length=128)),
                ('cpu_use', models.FloatField(default=0)),
                ('mem_free', models.FloatField(default=0)),
                ('disk_read', models.FloatField(default=0)),
                ('disk_write', models.FloatField(default=0)),
                ('upload_success', models.IntegerField(default=0)),
                ('yuce_success', models.IntegerField(default=0)),
                ('network', models.CharField(default='', max_length=128)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]