import openai
from preprocess import embed
from sqlalchemy.orm import Session
from models import ActTable
from config import config

class ChatModule:
    def __init__(self, api_key=config.OPENAI_API_KEY, model='gpt-4o'):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key
        self.system_prompt = """
You are the official chatbot for the Construction Industry Technology Institute. 
Provide clear, accurate information on construction regulations, policies, qualifications, and safety.
Answer in Polite Korean. 
If the question is not related to construction, please say "건설 관련 질문이 아닙니다."
If you can't find the answer in the given context, please say "잘 모르겟습니다."
"""

    def retrieve_docs(self, question_content, db: Session, k=5):
        query_vector = embed(question_content)
        items = db.query(ActTable).order_by(ActTable.act_vector.l2_distance(query_vector)).limit(k).all()
        if not items:
            return None

        relevant_docs = [{"act_name": item.act_name, "act_content": item.act_content} for item in items]
        return relevant_docs

    def generate_answer(self, query):
        response = openai.chat.completions.create(
            model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content.strip()
