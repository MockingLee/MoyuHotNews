# Generated by Django 2.1 on 2019-10-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_news_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='expired',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
