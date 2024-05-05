# yourappname/migrations/0002_auto.py

from django.db import migrations

def create_tags(apps, schema_editor):
    Tag = apps.get_model('videoupload', 'Tag')
    Tag.objects.create(name='Beginner')
    Tag.objects.create(name='Intermediate')
    Tag.objects.create(name='Advanced')

class Migration(migrations.Migration):

    dependencies = [
        ('videoupload', '0001_initial'),  # Make sure to use the correct initial migration file
    ]

    operations = [
        migrations.RunPython(create_tags),
    ]
