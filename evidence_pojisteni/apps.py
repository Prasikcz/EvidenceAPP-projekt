from django.apps import AppConfig


class EvidencePojisteniConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'evidence_pojisteni'

    def ready(self):
        import evidence_pojisteni.signals