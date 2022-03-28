# Generated by Django 4.0.3 on 2022-03-28 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_role',
            field=models.CharField(choices=[('Local_Building_Manager', 'Local_Building_Manager'), ('Property_Manager', 'Property_Manager'), ('MAH_Employee', 'MAH_Employee')], default='MAH_Employee', max_length=100, null=True),
        ),
    ]
