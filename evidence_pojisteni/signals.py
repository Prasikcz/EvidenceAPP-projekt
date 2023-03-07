from django.db.models.signals import post_save

from django.contrib.auth.models import User, Group
from .models import Klient


def klient_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='klient')
        instance.groups.add(group)

        Klient.objects.create(
            user=instance,
            e_mail=instance.email,
            jmeno=instance.first_name,
            prijmeni=instance.last_name,
            )
post_save.connect(klient_profile, sender=User)
 


