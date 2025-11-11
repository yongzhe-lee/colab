"""
JupyterHub 앱 설정
"""
from django.apps import AppConfig


class JupyterhubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.jupyterhub'
    verbose_name = 'JupyterHub 통합'



