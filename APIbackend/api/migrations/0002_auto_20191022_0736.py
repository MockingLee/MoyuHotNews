# Generated by Django 2.2.6 on 2019-10-22 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
        migrations.AddField(
            model_name='news',
            name='site',
            field=models.CharField(default='0', max_length=7, verbose_name='news site type'),
        ),
    ]