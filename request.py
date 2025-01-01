from pydantic import BaseModel, Field, field_validator

class QuestionRequest(BaseModel):
    question_content: str # 질문 내용
    call_path: str = Field(default="api", pattern="^(user|api)$") # api(default) 또는 user

    class Config:
        json_schema_extra = {
            "example": {
                "question_content": "건설산업기본법의 기본 취지는 무엇인가",
                "call_path": "api"
            }
        }

class UpdateActDBRequest(BaseModel):
    act_pdf_path: str = Field(..., description="PDF 파일 경로")