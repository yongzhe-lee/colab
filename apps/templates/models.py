from django.db import models
from apps.core.models import BaseModel


class TemplateCategory(models.Model):
    """템플릿 카테고리"""
    name = models.CharField(max_length=100, unique=True, verbose_name='카테고리명')
    description = models.TextField(blank=True, verbose_name='설명')
    order = models.IntegerField(default=0, verbose_name='정렬 순서')

    class Meta:
        verbose_name = '템플릿 카테고리'
        verbose_name_plural = '템플릿 카테고리'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Template(BaseModel):
    """Python 코드 템플릿"""
    CATEGORY_CHOICES = [
        ('grid', '그리드 조회'),
        ('chart', '차트 조회'),
        ('regression', '회귀분석'),
        ('classification', '분류분석'),
        ('clustering', '클러스터링'),
        ('data_processing', '데이터 처리'),
        ('other', '기타'),
    ]

    name = models.CharField(max_length=200, verbose_name='템플릿명')
    category = models.ForeignKey(
        TemplateCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='카테고리'
    )
    category_type = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='other',
        verbose_name='카테고리 타입'
    )
    description = models.TextField(blank=True, verbose_name='설명')
    code = models.TextField(verbose_name='템플릿 코드')
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    is_public = models.BooleanField(default=True, verbose_name='공개')
    usage_count = models.IntegerField(default=0, verbose_name='사용 횟수')
    tags = models.CharField(max_length=500, blank=True, verbose_name='태그')

    class Meta:
        verbose_name = '템플릿'
        verbose_name_plural = '템플릿'
        ordering = ['category_type', 'name']

    def __str__(self):
        return self.name

