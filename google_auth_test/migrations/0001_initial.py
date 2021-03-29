# Generated by Django 3.1.7 on 2021-03-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrUser',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='users_photo')),
                ('user_info', models.TextField()),
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
