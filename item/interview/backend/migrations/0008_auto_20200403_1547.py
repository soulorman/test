# Generated by Django 2.0 on 2020-04-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20200402_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='scores',
            field=models.CharField(default='未批改简答题', max_length=32),
        ),
    ]
