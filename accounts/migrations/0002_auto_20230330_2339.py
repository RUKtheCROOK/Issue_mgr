# Generated by Django 4.1.7 on 2023-03-30 23:39

from django.db import migrations

def populate_teams(apps, schemaeditor):
    defaults = {
        'a': 'the a team',
        'b': 'the b team',
        'c': 'the c team',
    }
    Team = apps.get_model('accounts', 'Team')
    for key, desc in defaults.items():
        team_obj = Team(name=key, description=desc)
        team_obj.save()

def populate_roles(apps, schemaeditor):
    defaults = {
        'dev': 'dev role',
        'scrum mate': 'scrum mate role',
        'product owner': 'product owner role',
    }
    Role = apps.get_model('accounts', 'Role')
    for key, desc in defaults.items():
        role_obj = Role(name=key, description=desc)
        role_obj.save()
class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_teams),
        migrations.RunPython(populate_roles),
    ]
