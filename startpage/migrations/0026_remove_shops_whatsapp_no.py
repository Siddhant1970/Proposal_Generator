# Generated by Django 3.1.2 on 2022-11-13 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0025_auto_20221114_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shops',
            name='whatsapp_no',
        ),
    ]
