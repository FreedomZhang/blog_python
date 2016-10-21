# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 06:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleID', models.CharField(default='', max_length=50, verbose_name='ID')),
                ('className', models.CharField(max_length=50, verbose_name='\u5206\u7c7b')),
                ('titele', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('article', models.TextField(max_length=5000, verbose_name='\u5185\u5bb9')),
                ('releaseTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('author', models.CharField(max_length=50, verbose_name='\u4f5c\u8005')),
                ('clickVolume', models.CharField(max_length=50, verbose_name='\u70b9\u51fb\u91cf')),
                ('tstate', models.CharField(max_length=50, verbose_name='\u72b6\u6001')),
                ('labels', models.CharField(max_length=50, verbose_name='\u6807\u7b7e')),
                ('enclosures', models.CharField(max_length=50, verbose_name='\u9644\u4ef6\u5730\u5740')),
                ('reserve1', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb51')),
                ('reserve2', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb52')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentID', models.CharField(default='', max_length=50, verbose_name='ID')),
                ('articleID', models.CharField(max_length=50, verbose_name='\u6587\u7ae0id')),
                ('content', models.CharField(max_length=50, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('commentTime', models.DateTimeField(default=datetime.datetime(2016, 10, 21, 6, 17, 28, 966000, tzinfo=utc), verbose_name='\u8bc4\u8bba\u65f6\u95f4')),
                ('commentPel', models.CharField(max_length=50, verbose_name='\u8bc4\u8bba\u4eba')),
                ('reserve1', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb51')),
                ('reserve2', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb52')),
            ],
        ),
        migrations.CreateModel(
            name='Enclosure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enclosureID', models.CharField(default='', max_length=50, verbose_name='ID')),
                ('enclosureType', models.CharField(max_length=50, verbose_name='\u6587\u4ef6\u7c7b\u578b')),
                ('lname', models.CharField(max_length=50, verbose_name='\u539f\u540d\u79f0')),
                ('wname', models.CharField(max_length=50, verbose_name='\u6587\u4ef6\u552f\u4e00\u540d\u79f0')),
                ('eroute', models.CharField(max_length=50, verbose_name='\u6587\u4ef6\u8def\u5f84')),
                ('etime', models.DateTimeField(default=datetime.datetime(2016, 10, 21, 6, 17, 28, 966000, tzinfo=utc))),
                ('reserve1', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb51')),
                ('reserve2', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb52')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelID', models.CharField(default='', max_length=50, verbose_name='ID')),
                ('labelName', models.CharField(max_length=50, verbose_name='\u6807\u7b7e\u540d\u79f0')),
                ('remarks', models.TextField(max_length=500, verbose_name='\u5907\u6ce8')),
                ('reserve1', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb51')),
                ('reserve2', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb52')),
            ],
        ),
        migrations.CreateModel(
            name='Tclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classID', models.CharField(default='', max_length=50, verbose_name='ID')),
                ('className', models.CharField(max_length=50, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('remarks', models.TextField(max_length=500, verbose_name='\u5907\u6ce8')),
                ('parentID', models.CharField(max_length=50, verbose_name='\u7236\u7ea7ID')),
                ('reserve1', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb51')),
                ('reserve2', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb52')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleID', models.CharField(default='', max_length=50, verbose_name='ID')),
                ('titleName', models.CharField(max_length=50, verbose_name='\u6807\u9898\u540d\u79f0')),
                ('remarks', models.TextField(max_length=500, verbose_name='\u5907\u6ce8')),
                ('resUrl', models.CharField(max_length=100, verbose_name='\u9884\u7559URL')),
                ('reserve1', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb51')),
                ('reserve2', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb52')),
            ],
        ),
        migrations.CreateModel(
            name='Tstate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statID', models.CharField(default='', max_length=50, verbose_name='ID')),
                ('stateName', models.CharField(max_length=50, verbose_name='\u72b6\u6001\u540d\u79f0')),
                ('remarks', models.TextField(max_length=500, verbose_name='\u5907\u6ce8')),
                ('reserve1', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb51')),
                ('reserve2', models.CharField(max_length=100, verbose_name='\u9884\u7559\u5b57\u6bb52')),
            ],
        ),
    ]
