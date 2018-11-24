# Generated by Django 2.1.3 on 2018-11-24 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclass',
            name='class_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='studentclass',
            name='class_no',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='studentclass',
            unique_together=set(),
        ),
    ]