from django.apps import AppConfig


class AppglobalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppGlobal'

class DirectConfig(AppConfig):
    name = 'direct'