# Generated by Django 5.1.1 on 2024-10-01 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_user_profile_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='county',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='post_or_zipcode',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='street_address1',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='street_address2',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='town_or_city',
        ),
    ]
