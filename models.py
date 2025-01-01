from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base
from pgvector.sqlalchemy.vector import VECTOR  # sqlalchemy.vector 임포트

# QA 테이블
class QATable(Base):
    __tablename__ = "t_qa"
    qa_id = Column(Integer, primary_key=True, index=True)
    qa_content = Column(String, index=True)
    qa_vector = Column(VECTOR)  # 벡터 필드를 VECTOR 클래스로 정의
    
    # extend_existing=True 추가
    __table_args__ = {'extend_existing': True}

## 우선적으로 테스트 해보고자 함
# 법령 테이블
class ActTable(Base):
    __tablename__ = "t_act"
    act_id = Column(Integer, primary_key=True, index=True)
    act_content = Column(String, index=True)
    act_vector = Column(VECTOR)  # 벡터 필드를 VECTOR 클래스로 정의
    act_name = Column(String, index=True)

    # extend_existing=True 추가
    __table_args__ = {'extend_existing': True}

# 메트릭 테이블
class MetricTable(Base):
    __tablename__ = "t_metric"
    metric_id = Column(Integer, primary_key=True, index=True)
    s_datetime = Column(String)  # 호출시간
    question = Column(String)  # 질의내용
    context = Column(String)  # 검색된 문맥
    answer = Column(String)  # 생성된 답변
    t_retrieval = Column(Integer)  # 검색 수행 시간(ms)
    t_llm = Column(Integer)  # LLM 수행시간(ms)
    t_total = Column(Integer)  # 전체 서버 수행 시간(ms)
    e_datetime = Column(String)  # 응답시간 - date time
    tokens_prompt = Column(Integer)  # 입력 토큰: Q+C
    tokens_completion = Column(Integer)  # 생성 토큰: A
    tokens_total = Column(Integer)  # 전체 토큰: Q+C+A
    model_name = Column(String)  # 사용된 LLM 모델

    # extend_existing=True 추가
    __table_args__ = {'extend_existing': True}

