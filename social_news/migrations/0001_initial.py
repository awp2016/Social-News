# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 09:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('upvotes', models.IntegerField(default=0)),
                ('content', models.TextField(default='')),
                ('users_liked', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]