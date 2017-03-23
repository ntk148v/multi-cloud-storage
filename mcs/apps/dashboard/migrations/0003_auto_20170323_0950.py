# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170322_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='data',
        ),
        migrations.RemoveField(
            model_name='file',
            name='parent_path',
        ),
        migrations.RemoveField(
            model_name='file',
            name='path',
        ),
        migrations.AddField(
            model_name='file',
            name='content',
            field=models.FileField(null=True, upload_to=b'', verbose_name='content'),
        ),
        migrations.AddField(
            model_name='file',
            name='is_root',
            field=models.BooleanField(default=False, verbose_name='is_root'),
        ),
        migrations.AddField(
            model_name='file',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='dashboard.File', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='file',
            name='is_folder',
            field=models.BooleanField(default=True, verbose_name='is_folder'),
        ),
        migrations.AlterField(
            model_name='file',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True, verbose_name='last_modified'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.IntegerField(editable=False, null=True, verbose_name='size'),
        ),
    ]
