# Generated by Django 3.1.2 on 2022-06-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0021_delete_raja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='whatsapp_no',
            field=models.BigIntegerField(default=0),
        ),
    ]