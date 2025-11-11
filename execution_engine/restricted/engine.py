"""
RestrictedPython 기반 안전한 코드 실행 엔진
"""
import time
import sys
from io import StringIO
from typing import Dict, Any, Optional, Tuple
from RestrictedPython import compile_restricted
from RestrictedPython.Guards import safe_builtins, guarded_iter_unpack, guarded_unpacking

from execution_engine.base import ExecutionEngine
from django.conf import settings


class RestrictedPythonEngine(ExecutionEngine):
    """RestrictedPython을 사용한 안전한 코드 실행 엔진"""

    def __init__(self):
        self.allowed_modules = settings.PYTHON_EXECUTION.get('ALLOWED_MODULES', [])
        self.restricted_functions = settings.PYTHON_EXECUTION.get('RESTRICTED_FUNCTIONS', [])

    def _get_allowed_imports(self) -> Dict[str, Any]:
        """허용된 모듈만 import 가능하도록 설정"""
        allowed_imports = {}
        
        for module_name in self.allowed_modules:
            try:
                allowed_imports[module_name] = __import__(module_name)
            except ImportError:
                # 모듈이 설치되지 않은 경우 무시
                pass
        
        return allowed_imports

    def _create_safe_globals(self) -> Dict[str, Any]:
        """안전한 전역 변수 환경 생성"""
        safe_globals = {
            '__builtins__': safe_builtins.copy(),
            '_print_': self._safe_print,
            '_getitem_': self._safe_getitem,
            '_iter_unpack_': guarded_iter_unpack,
            '_unpacking_': guarded_unpacking,
        }
        
        # 허용된 모듈 추가
        safe_globals.update(self._get_allowed_imports())
        
        return safe_globals

    def _safe_print(self, *args, **kwargs):
        """안전한 print 함수"""
        return print(*args, **kwargs)

    def _safe_getitem(self, obj, key):
        """안전한 getitem"""
        return obj[key]

    def validate_code(self, code: str) -> Tuple[bool, Optional[str]]:
        """
        코드 유효성 검사
        """
        if not code or not code.strip():
            return False, "코드가 비어있습니다."
        
        # 위험한 함수 사용 검사
        for func in self.restricted_functions:
            if func in code:
                return False, f"허용되지 않은 함수 '{func}'가 사용되었습니다."
        
        # 컴파일 시도
        try:
            compile_restricted(code)
        except SyntaxError as e:
            return False, f"문법 오류: {str(e)}"
        except Exception as e:
            return False, f"코드 검증 오류: {str(e)}"
        
        return True, None

    def execute(
        self,
        code: str,
        timeout: int = 30,
        max_memory: int = 512,
        **kwargs
    ) -> Dict[str, Any]:
        """
        RestrictedPython을 사용하여 코드 실행
        """
        start_time = time.time()
        output_buffer = StringIO()
        error_buffer = StringIO()
        
        # 코드 검증
        is_valid, error_msg = self.validate_code(code)
        if not is_valid:
            return {
                'status': 'error',
                'output': '',
                'error': error_msg,
                'execution_time': 0,
                'memory_used': 0
            }
        
        try:
            # 코드 컴파일
            byte_code = compile_restricted(code)
            if byte_code.errors:
                return {
                    'status': 'error',
                    'output': '',
                    'error': '; '.join(byte_code.errors),
                    'execution_time': time.time() - start_time,
                    'memory_used': 0
                }
            
            # 안전한 실행 환경 설정
            safe_globals = self._create_safe_globals()
            safe_locals = {}
            
            # stdout 리다이렉트
            old_stdout = sys.stdout
            old_stderr = sys.stderr
            sys.stdout = output_buffer
            sys.stderr = error_buffer
            
            try:
                # 코드 실행
                exec(byte_code.code, safe_globals, safe_locals)
                
                # 출력 수집
                output = output_buffer.getvalue()
                error = error_buffer.getvalue()
                
                execution_time = time.time() - start_time
                
                # 타임아웃 체크
                if execution_time > timeout:
                    return {
                        'status': 'timeout',
                        'output': output,
                        'error': f'실행 시간이 {timeout}초를 초과했습니다.',
                        'execution_time': execution_time,
                        'memory_used': 0
                    }
                
                if error:
                    return {
                        'status': 'error',
                        'output': output,
                        'error': error,
                        'execution_time': execution_time,
                        'memory_used': 0
                    }
                
                return {
                    'status': 'success',
                    'output': output,
                    'error': None,
                    'execution_time': execution_time,
                    'memory_used': 0  # 메모리 측정은 추후 구현
                }
                
            finally:
                # stdout/stderr 복원
                sys.stdout = old_stdout
                sys.stderr = old_stderr
                
        except Exception as e:
            execution_time = time.time() - start_time
            return {
                'status': 'error',
                'output': output_buffer.getvalue(),
                'error': str(e),
                'execution_time': execution_time,
                'memory_used': 0
            }

