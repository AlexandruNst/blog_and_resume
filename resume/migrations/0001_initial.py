# Generated by Django 2.2.12 on 2020-06-10 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('SK', 'Skills'), ('EX', 'Experience'), ('ED', 'Education'), ('TI', 'Technical Interests')], max_length=2)),
                ('title', models.CharField(max_length=200)),
                ('timeframe', models.CharField(blank=True, max_length=200)),
                ('text', models.TextField(blank=True)),
            ],
        ),
    ]
