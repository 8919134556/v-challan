# Generated by Django 3.2.8 on 2022-07-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vechile_register',
            name='vechile_type',
            field=models.CharField(db_column='vechile_type', max_length=50, null=True, verbose_name='vechile_type'),
        ),
    ]
