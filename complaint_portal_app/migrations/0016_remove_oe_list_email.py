# Generated by Django 4.2 on 2023-06-20 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_portal_app', '0015_oe_list_oe_premise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oe_list',
            name='email',
        ),
    ]