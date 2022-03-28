# Generated by Django 3.2 on 2022-03-16 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=200)),
                ('user_role', models.CharField(blank=True, max_length=50)),
                ('user_email', models.CharField(blank=True, max_length=50)),
                ('user_email_1', models.CharField(blank=True, max_length=50)),
                ('user_contact_num', models.IntegerField(blank=True, default=0)),
                ('user_skills', models.CharField(blank=True, max_length=250)),
                ('user_password', models.CharField(blank=True, max_length=100)),
                ('user_address_1', models.CharField(blank=True, max_length=200)),
                ('user_address_2', models.CharField(blank=True, max_length=200)),
                ('user_city', models.CharField(blank=True, max_length=100)),
                ('user_state', models.CharField(blank=True, max_length=100)),
                ('user_profile_created_check', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
