"""
기본 실행 엔진 인터페이스
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, Tuple


class ExecutionEngine(ABC):
    """코드 실행 엔진 기본 클래스"""

    @abstractmethod
    def execute(
        self,
        code: str,
        timeout: int = 30,
        max_memory: int = 512,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Python 코드를 실행하고 결과를 반환

        Args:
            code: 실행할 Python 코드
            timeout: 실행 시간 제한 (초)
            max_memory: 최대 메모리 사용량 (MB)
            **kwargs: 추가 옵션

        Returns:
            {
                'status': 'success' | 'error' | 'timeout',
                'output': str,
                'error': str | None,
                'execution_time': float,
                'memory_used': int
            }
        """
        pass

    @abstractmethod
    def validate_code(self, code: str) -> Tuple[bool, Optional[str]]:
        """
        코드 유효성 검사

        Args:
            code: 검사할 코드

        Returns:
            (is_valid, error_message)
        """
        pass

