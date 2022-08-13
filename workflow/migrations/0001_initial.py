# Generated by Django 3.2.14 on 2022-08-13 11:05

import auto_prefetch
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('siteapp', '0069_alter_project_import_record'),
        ('controls', '0080_auto_20220725_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkflowImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('name', models.CharField(blank=True, help_text='Descriptive name', max_length=100, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unique identifier')),
                ('workflow', models.JSONField(blank=True, default=dict, help_text='Workflow object')),
                ('rules', models.JSONField(blank=True, default=list, help_text='Rules list')),
                ('tags', models.ManyToManyField(blank=True, related_name='workflowimage', to='siteapp.Tag')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'prefetch_manager',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowInstanceSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('name', models.CharField(blank=True, help_text='Descriptive name', max_length=100, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unique identifier')),
                ('description', models.CharField(blank=True, help_text='Brief description', max_length=250, null=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='workflowinstanceset', to='siteapp.Tag')),
                ('workflowimage', auto_prefetch.ForeignKey(help_text='WorkflowImage', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflowinstancesets', to='workflow.workflowimage')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'prefetch_manager',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('name', models.CharField(blank=True, help_text='Descriptive name', max_length=100, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unique identifier')),
                ('workflow', models.JSONField(blank=True, default=dict, help_text='Workflow object')),
                ('rules', models.JSONField(blank=True, default=list, help_text='Rules list')),
                ('log', models.JSONField(blank=True, default=list, help_text='Log entries')),
                ('system', auto_prefetch.ForeignKey(blank=True, help_text='System', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workflowinstances', to='controls.system')),
                ('tags', models.ManyToManyField(blank=True, related_name='workflowinstance', to='siteapp.Tag')),
                ('workflowimage', auto_prefetch.ForeignKey(help_text='WorkflowImage', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflowinstances', to='workflow.workflowimage')),
                ('workflowinstanceset', auto_prefetch.ForeignKey(blank=True, help_text='System', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflowinstances', to='workflow.workflowinstanceset')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'prefetch_manager',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
