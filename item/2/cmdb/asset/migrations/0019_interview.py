# Generated by Django 2.0 on 2020-02-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0018_auto_20200113_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField(default=0)),
                ('question_type', models.CharField(default='无', max_length=64)),
                ('question_answer', models.TextField(default='无')),
                ('scores', models.IntegerField(default=0)),
                ('update_time', models.DateTimeField()),
            ],
        ),
    ]
