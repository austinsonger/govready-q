# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('guidedmodules', '0016_auto_20170313_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_hash', models.CharField(help_text='A hash of the asset binary content, as provided by the source.', max_length=64)),
                ('file', models.FileField(help_text='The attached file.', upload_to='guidedmodules/module-assets')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('extra', jsonfield.fields.JSONField(blank=True, help_text='Additional information stored with this object.')),
                ('source', models.ForeignKey(help_text='The source of the asset.', on_delete=django.db.models.deletion.CASCADE, to='guidedmodules.ModuleSource')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleAssetPack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basepath', models.SlugField(help_text='The base path of all assets in this pack.', max_length=100)),
                ('paths', jsonfield.fields.JSONField(help_text='A dictionary mapping file paths to the content_hashes of assets included in the assets field of this instance.')),
                ('total_hash', models.CharField(help_text='A SHA256 hash over the paths and the content_hashes of the assets.', max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('extra', jsonfield.fields.JSONField(blank=True, help_text='Additional information stored with this object.')),
                ('assets', models.ManyToManyField(help_text='The assets linked to this pack.', to='guidedmodules.ModuleAsset')),
                ('source', models.ForeignKey(help_text='The source of these assets.', on_delete=django.db.models.deletion.CASCADE, to='guidedmodules.ModuleSource')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='assets',
            field=models.ForeignKey(blank=True, help_text='A mapping from asset paths to ModuleAsset instances with the binary content of the asset.', null=True, on_delete=django.db.models.deletion.CASCADE, to='guidedmodules.ModuleAssetPack'),
        ),
        migrations.AlterUniqueTogether(
            name='moduleassetpack',
            unique_together=set([('source', 'total_hash')]),
        ),
        migrations.AlterUniqueTogether(
            name='moduleasset',
            unique_together=set([('source', 'content_hash')]),
        ),
    ]