from pydantic import BaseModel
from decimal import Decimal

class Response(BaseModel):
    act_id: str
    act_name: str
    act_content: str
    similarity: Decimal

class ListResponse(BaseModel):
    documents: list[Response]

class ChatBot_Response(BaseModel):
    question_content: str
    answer_content: str
    context: ListResponse