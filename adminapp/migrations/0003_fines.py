# Generated by Django 3.2.8 on 2022-07-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_vechile_register_vechile_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fines',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('drunk', models.CharField(db_column='drunk', max_length=50, verbose_name='Drunk')),
                ('without_helmate', models.CharField(db_column='without_helmate', max_length=50, verbose_name='Without_Helmate')),
                ('without_licence', models.CharField(db_column='without_licence', max_length=50, verbose_name='Without_Licence')),
                ('over_speed', models.CharField(db_column='over_speed', max_length=50, verbose_name='Over_Speed')),
                ('signal_jumping', models.CharField(db_column='signal_jumping', max_length=50, verbose_name='Signal_Jumping')),
                ('juvenile_driving', models.CharField(db_column='juvenile_driving', max_length=50, verbose_name='Juvenile_driving')),
            ],
            options={
                'db_table': 'Fines',
            },
        ),
    ]
