# Generated by Django 5.0.6 on 2024-09-11 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htdtech', '0003_alter_prevyearinfo_allottedlist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prevyearinfo',
            name='Serialno',
        ),
        migrations.DeleteModel(
            name='Serialno',
        ),
    ]
