
from typing import TypedDict
from pydantic import BaseModel
class Blog(BaseModel):
    title:str
    content:str

class State(TypedDict):
    topic:str
    blog:Blog
    language:str
