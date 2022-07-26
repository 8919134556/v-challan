# Generated by Django 3.2.8 on 2022-07-16 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='V_Fines',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(db_column='user_name', max_length=50, verbose_name='User_Name')),
                ('user_lastname', models.CharField(db_column='user_lastname', max_length=50, verbose_name='User_Lastname')),
                ('vechile_year', models.CharField(db_column='vechile_year', max_length=50, verbose_name='Vechile_Year')),
                ('vechile_make', models.CharField(db_column='vechile_make', max_length=50, verbose_name='Vechile_Make')),
                ('vechile_color', models.CharField(db_column='vechile_color', max_length=50, verbose_name='Vechile_Color')),
                ('vechile_number', models.CharField(db_column='vechile_number', max_length=50, verbose_name='vechile_number')),
                ('vechile_type', models.CharField(db_column='vechile_type', max_length=50, null=True, verbose_name='vechile_type')),
                ('fine', models.CharField(db_column='fine', max_length=50, null=True, verbose_name='fine')),
                ('vechile_image', models.FileField(blank=True, db_column='Vechile_image', upload_to='User/fins/', verbose_name='Vechile_image')),
                ('datetime_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'V_Fines',
            },
        ),
    ]
