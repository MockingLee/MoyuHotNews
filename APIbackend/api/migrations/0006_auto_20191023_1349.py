# Generated by Django 2.1 on 2019-10-23 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_news_expired'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='expired',
            new_name='generation',
        ),
    ]
