# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='forgot_pin',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_email_verified',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_forgot',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sur_name',
        ),
    ]
