import os
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from apps.core.models import BaseModel


def user_code_directory_path(instance, filename):
    """사용자별 코드 파일 저장 경로"""
    return f'code_files/{instance.user.id}/{filename}'


class CodeFile(BaseModel):
    """사용자 Python 코드 파일"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='사용자')
    name = models.CharField(max_length=255, verbose_name='파일명')
    file = models.FileField(
        upload_to=user_code_directory_path,
        null=True,
        blank=True,
        verbose_name='파일'
    )
    code = models.TextField(verbose_name='코드 내용')
    file_type = models.CharField(
        max_length=10,
        choices=[('py', 'Python'), ('ipynb', 'Jupyter Notebook')],
        default='py',
        verbose_name='파일 타입'
    )
    description = models.TextField(blank=True, verbose_name='설명')
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    last_executed_at = models.DateTimeField(null=True, blank=True, verbose_name='마지막 실행일시')

    class Meta:
        verbose_name = '코드 파일'
        verbose_name_plural = '코드 파일'
        ordering = ['-updated_at']
        unique_together = ['user', 'name']

    def __str__(self):
        return f'{self.user.username} - {self.name}'

    def get_file_size(self):
        """파일 크기 반환 (KB)"""
        if self.file and self.file.size:
            return round(self.file.size / 1024, 2)
        return 0

