# Generated by Django 2.0.13 on 2019-05-19 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('content', models.CharField(max_length=2048)),
            ],
        ),
    ]
