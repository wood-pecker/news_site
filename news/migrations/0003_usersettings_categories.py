# Generated by Django 4.2.8 on 2024-03-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_usersettings_is_phone_verified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='categories',
            field=models.ManyToManyField(related_name='users', to='news.category'),
        ),
    ]
