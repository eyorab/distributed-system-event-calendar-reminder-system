# Generated by Django 5.1.4 on 2025-01-03 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user_id',
        ),
    ]
