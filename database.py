from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from config import config

# 데이터베이스 엔진 생성
engine = create_engine(config.PG_DATABASE_URL)

# 세션 만들기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모델 정의
Base = declarative_base()

# 모델 생성
Base.metadata.create_all(engine)

# 세션 만들기
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()