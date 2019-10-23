# Generated by Django 2.1 on 2019-10-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191022_0736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={},
        ),
        migrations.RemoveField(
            model_name='news',
            name='img',
        ),
        migrations.RemoveField(
            model_name='news',
            name='site',
        ),
        migrations.AddField(
            model_name='news',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='news',
            name='site_type',
            field=models.CharField(blank=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]
