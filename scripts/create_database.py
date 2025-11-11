"""
PostgreSQL 데이터베이스 및 스키마 생성 스크립트
"""
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# 데이터베이스 연결 정보
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'postgres',
    'database': 'postgres'  # 기본 postgres DB에 연결
}

def create_database_and_schema():
    """데이터베이스와 스키마 생성"""
    try:
        # 기본 postgres 데이터베이스에 연결
        print("PostgreSQL 서버에 연결 중...")
        conn = psycopg2.connect(**DB_CONFIG)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # 데이터베이스 존재 여부 확인
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'postgres'")
        exists = cursor.fetchone()
        
        if not exists:
            print("기본 postgres 데이터베이스가 존재하지 않습니다.")
            return False
        
        # colab 스키마 생성 (postgres 데이터베이스 내)
        print("colab 스키마 생성 중...")
        cursor.execute("""
            SELECT schema_name 
            FROM information_schema.schemata 
            WHERE schema_name = 'colab'
        """)
        
        if not cursor.fetchone():
            cursor.execute("CREATE SCHEMA colab")
            print("[OK] colab 스키마가 생성되었습니다.")
        else:
            print("[OK] colab 스키마가 이미 존재합니다.")
        
        # 스키마 권한 설정
        cursor.execute("GRANT ALL PRIVILEGES ON SCHEMA colab TO postgres")
        cursor.execute("GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA colab TO postgres")
        cursor.execute("GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA colab TO postgres")
        cursor.execute("ALTER DEFAULT PRIVILEGES IN SCHEMA colab GRANT ALL ON TABLES TO postgres")
        cursor.execute("ALTER DEFAULT PRIVILEGES IN SCHEMA colab GRANT ALL ON SEQUENCES TO postgres")
        print("[OK] 스키마 권한이 설정되었습니다.")
        
        cursor.close()
        conn.close()
        
        print("\n[SUCCESS] 데이터베이스 설정이 완료되었습니다!")
        print("   - 데이터베이스: postgres")
        print("   - 스키마: colab")
        print("   - 사용자: postgres")
        return True
        
    except psycopg2.OperationalError as e:
        print(f"[ERROR] PostgreSQL 연결 오류: {e}")
        print("\n다음 사항을 확인해주세요:")
        print("1. PostgreSQL 서버가 실행 중인지 확인")
        print("2. 연결 정보가 올바른지 확인")
        print("3. psycopg2 패키지가 설치되어 있는지 확인 (pip install psycopg2-binary)")
        return False
    except Exception as e:
        print(f"[ERROR] 오류 발생: {e}")
        return False

if __name__ == '__main__':
    create_database_and_schema()

