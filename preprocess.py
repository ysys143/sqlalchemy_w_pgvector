import openai 
import re
from config import config

def embed(text_input):
    create_embedding_response = openai.embeddings.create(
        input=text_input,
        model=config.EMBEDDING_MODEL
    )
    return create_embedding_response.data[0].embedding

def get_act_name(text_input):
    
    act_name = "건설산업기본법"

    if re.search(r"제\s*\d+장", text_input):
        act_name += " " + re.search(r"제\s*\d+장", text_input).group(0)

    if re.search(r"제\s*\d+조", text_input):
        act_name += " " + re.search(r"제\s*\d+조", text_input).group(0)

    if re.search(r"제\s*\d+조(?:의\d+)", text_input):
        act_name += " " + re.search(r"제\s*\d+조(?:의\d+)", text_input).group(0)

    return act_name