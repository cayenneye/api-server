# Generated by Django 4.2.7 on 2024-01-27 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manas_id', '0012_alter_manasid_extra_preferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manasid',
            name='course',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Preparation'), (2, 'Bachelor First'), (3, 'Bachelor Second'), (4, 'Bachelor Third'), (5, 'Bachelor Fourth'), (6, 'Applicant')]),
        ),
    ]