# Generated by Django 4.0 on 2022-11-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0027_shops_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='shops',
            name='status2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shops',
            name='Date',
            field=models.DateField(blank=True, verbose_name='Proposal Date(dd/mm/yyyy)'),
        ),
    ]