# Generated by Django 4.2.7 on 2024-02-16 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_user_subscription_started_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='born_at',
        ),
    ]
