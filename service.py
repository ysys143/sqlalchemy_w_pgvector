from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database import get_db
from request import QuestionRequest
from preprocess import embed
from utils import ChatModule
from config import config

from response import ListResponse, ChatBot_Response

router = APIRouter()
chat_module = ChatModule(api_key=config.OPENAI_API_KEY, model=config.GPT_MODEL)

@router.post("/retrieve")
async def retrieve_context(question: QuestionRequest, db: Session = Depends(get_db), k=5):
    return chat_module.retrieve_docs(question.question_content, db, k)

@router.post("/chatbot")
async def retrieve_and_generate(question: QuestionRequest, db: Session = Depends(get_db)):

    # 문서 조회
    docs = chat_module.retrieve_docs(question.question_content, db)
    if not docs:
        raise HTTPException(status_code=404, detail="Documents not found")

    # 증강된 쿼리 생성
    combined_docs = "\n".join([doc["act_content"] for doc in docs])
    query = f"""Given the following legal documents, answer the user's question. 
    \n\nLegal documents: {combined_docs}
    \n\nUser’s question: {question.question_content}
    \n\nAnswer:"""
    
    # 답변 생성
    answer = chat_module.generate_answer(query)

    # 문서 정보 추가
    documents = [{"act_name": doc["act_name"], "act_content": doc["act_content"]} for doc in docs]
    
    return {"answer": answer, "documents": documents}