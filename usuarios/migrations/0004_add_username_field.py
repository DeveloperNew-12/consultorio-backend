# Generated migration for adding username field

from django.db import migrations, models

def create_unique_usernames(apps, schema_editor):
    Usuario = apps.get_model('usuarios', 'Usuario')
    for i, usuario in enumerate(Usuario.objects.all(), 1):
        usuario.username = f'user{i}'
        usuario.save()

def reverse_username_creation(apps, schema_editor):
    # No need to do anything on reverse
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_increment_ids'),
    ]

    operations = [
        # First add the field without unique constraint
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='temp', max_length=50),
        ),
        # Populate unique usernames
        migrations.RunPython(create_unique_usernames, reverse_username_creation),
        # Now make it unique
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
