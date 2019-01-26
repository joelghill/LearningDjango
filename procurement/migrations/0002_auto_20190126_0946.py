# Generated by Django 2.1.5 on 2019-01-26 15:46

from django.db import migrations

def migrate_representatives(apps, scheme_editor):
    Supplier = apps.get_model('procurement', 'Supplier')
    for supplier in Supplier.objects.all():
        Representative = apps.get_model('procurement', 'Representative')
        rep = Representative();
        rep.name = supplier.representative_name
        rep.email = supplier.representative_email
        rep.supplier = supplier
        rep.save()

class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0003_representative'),
    ]

    operations = [
        migrations.RunPython(migrate_representatives),
    ]
