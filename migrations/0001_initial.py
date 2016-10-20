# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-20 10:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
            ],
            options={
                'verbose_name_plural': 'CATEGORY',
                'verbose_name': 'CATEGORY',
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('brief', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'EDITOR',
                'verbose_name': 'EDITOR',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
            ],
            options={
                'verbose_name_plural': 'MENU',
                'verbose_name': 'MENU',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('menu', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ghoster.Menu')),
            ],
            options={
                'verbose_name_plural': 'PAGE',
                'verbose_name': 'PAGE',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255)),
                ('content', models.TextField()),
                ('thumbnail', models.URLField(blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ghoster.Category')),
                ('editor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ghoster.Editor')),
                ('page', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ghoster.Page')),
            ],
            options={
                'verbose_name_plural': 'POST',
                'verbose_name': 'POST',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
            ],
            options={
                'verbose_name_plural': 'TAG',
                'verbose_name': 'TAG',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='ghoster.Tag'),
        ),
    ]