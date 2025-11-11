"""
API URL Configuration
"""
from django.urls import path, include

app_name = 'api'

urlpatterns = [
    # API 엔드포인트는 각 앱의 urls.py에서 정의
    # path('execute/', include('apps.execution.urls')),
    # path('templates/', include('apps.templates.urls')),
    # path('files/', include('apps.files.urls')),
]

