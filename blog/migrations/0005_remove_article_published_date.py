# Generated by Django 2.2.12 on 2020-06-05 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200605_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='published_date',
        ),
    ]
