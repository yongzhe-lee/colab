from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel


class ExecutionLog(BaseModel):
    """코드 실행 로그"""
    STATUS_CHOICES = [
        ('pending', '대기중'),
        ('running', '실행중'),
        ('success', '성공'),
        ('error', '오류'),
        ('timeout', '타임아웃'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='사용자')
    code = models.TextField(verbose_name='실행 코드')
    execution_mode = models.CharField(
        max_length=20,
        default='restricted',
        verbose_name='실행 모드'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='상태'
    )
    output = models.TextField(blank=True, null=True, verbose_name='출력 결과')
    error = models.TextField(blank=True, null=True, verbose_name='에러 메시지')
    execution_time = models.FloatField(null=True, blank=True, verbose_name='실행 시간(초)')
    memory_used = models.IntegerField(null=True, blank=True, verbose_name='메모리 사용량(MB)')

    class Meta:
        verbose_name = '실행 로그'
        verbose_name_plural = '실행 로그'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.status} - {self.created_at}'


class ExecutionResult(BaseModel):
    """코드 실행 결과 캐시"""
    code_hash = models.CharField(max_length=64, unique=True, verbose_name='코드 해시')
    output = models.TextField(verbose_name='출력 결과')
    execution_time = models.FloatField(verbose_name='실행 시간(초)')
    hit_count = models.IntegerField(default=0, verbose_name='캐시 히트 횟수')

    class Meta:
        verbose_name = '실행 결과 캐시'
        verbose_name_plural = '실행 결과 캐시'
        ordering = ['-hit_count', '-created_at']

    def __str__(self):
        return f'{self.code_hash[:16]}... - {self.hit_count} hits'

