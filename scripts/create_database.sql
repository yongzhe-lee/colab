-- PostgreSQL 데이터베이스 및 스키마 생성 SQL 스크립트
-- psql로 실행: psql -U postgres -f create_database.sql

-- colab 스키마 생성
CREATE SCHEMA IF NOT EXISTS colab;

-- 스키마 권한 설정
GRANT ALL PRIVILEGES ON SCHEMA colab TO postgres;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA colab TO postgres;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA colab TO postgres;

-- 기본 권한 설정
ALTER DEFAULT PRIVILEGES IN SCHEMA colab GRANT ALL ON TABLES TO postgres;
ALTER DEFAULT PRIVILEGES IN SCHEMA colab GRANT ALL ON SEQUENCES TO postgres;

-- 스키마 확인
SELECT schema_name 
FROM information_schema.schemata 
WHERE schema_name = 'colab';

