"""
실행 엔진 팩토리
"""
from django.conf import settings
from execution_engine.base import ExecutionEngine
from execution_engine.restricted.engine import RestrictedPythonEngine


class ExecutionEngineFactory:
    """실행 엔진 팩토리 클래스"""

    @staticmethod
    def create_engine(mode: str = None) -> ExecutionEngine:
        """
        실행 모드에 따라 적절한 실행 엔진 생성

        Args:
            mode: 'restricted' 또는 'docker'

        Returns:
            ExecutionEngine 인스턴스
        """
        if mode is None:
            mode = settings.PYTHON_EXECUTION.get('DEFAULT_MODE', 'restricted')
        
        if mode == 'restricted':
            return RestrictedPythonEngine()
        elif mode == 'docker':
            # Docker 엔진은 추후 구현
            raise NotImplementedError("Docker 실행 엔진은 아직 구현되지 않았습니다.")
        else:
            raise ValueError(f"지원하지 않는 실행 모드: {mode}")

