# Generated by Django 3.2.8 on 2022-07-18 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_alter_fines_image'),
        ('policeapp', '0002_auto_20220718_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='v_fines',
            name='user',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.fines'),
        ),
    ]
