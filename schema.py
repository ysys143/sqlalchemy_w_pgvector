from pydantic import BaseModel
from typing import List

class Act(BaseModel):
    act_name : str
    act_content : str
    act_vector : List[float]

    class Config:
        arbitrary_types_allowed=True
