# Generated by Django 2.0.8 on 2018-09-19 09:46

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_user', '0002_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The roles this user belongs to. A user will get all permissions granted to each of their roles.', related_name='user_set', related_query_name='user', to='drf_user.Role', verbose_name='Roles'),
        ),
    ]
