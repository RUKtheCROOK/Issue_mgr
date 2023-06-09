# Generated by Django 4.1.7 on 2023-03-31 01:42

from django.db import migrations

def populate_status(apps, schemaeditor):
    defaults = {
        'to do': 'to do',
        'in progress': 'in progress',
        'done': 'done',
    }
    Status = apps.get_model('issues', 'Status')
    for key, desc in defaults.items():
        status_obj = Status(name=key, description=desc)
        status_obj.save()

def populate_priority(apps, schemaeditor):
    defaults = {
        'low': 'low priority',
        'medium': 'medium priority',
        'high': 'high priority',
    }
    Priority = apps.get_model('issues', 'Priority')
    for key, desc in defaults.items():
        priority_obj = Priority(name=key, description=desc)
        priority_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status),
        migrations.RunPython(populate_priority),
    ]
