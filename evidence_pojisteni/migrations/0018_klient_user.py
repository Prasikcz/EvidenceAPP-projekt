# Generated by Django 3.2.6 on 2023-03-01 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evidence_pojisteni', '0017_auto_20230220_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]