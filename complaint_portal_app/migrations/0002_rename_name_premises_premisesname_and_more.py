# Generated by Django 4.2 on 2023-06-12 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_portal_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='premises',
            old_name='name',
            new_name='PremisesName',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='name',
            new_name='StateName',
        ),
    ]
