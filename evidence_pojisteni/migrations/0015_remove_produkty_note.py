# Generated by Django 3.2.6 on 2023-02-19 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evidence_pojisteni', '0014_produkty_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkty',
            name='note',
        ),
    ]
