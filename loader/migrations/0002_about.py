# Generated by Django 2.0.1 on 2018-01-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=600)),
            ],
        ),
    ]
