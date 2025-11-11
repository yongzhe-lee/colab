from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    """메인 페이지"""
    return render(request, 'core/index.html', {
        'title': 'Colab - Python 실행 환경'
    })


def health_check(request):
    """헬스 체크 엔드포인트"""
    return JsonResponse({
        'status': 'ok',
        'message': 'Colab 서버가 정상적으로 실행 중입니다.',
        'endpoints': {
            'admin': '/admin/',
            'api': '/api/v1/',
        }
    })

