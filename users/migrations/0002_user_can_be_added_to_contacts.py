# Generated by Django 4.2.3 on 2023-08-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='can_be_added_to_contacts',
            field=models.BooleanField(default=True),
        ),
    ]
