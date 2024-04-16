from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class LLM(Enum):
    GPT_35 = 1
    GPT_4 = 2


class LLMRequestBase(BaseModel):
    input: str  # <-- user's raw input
    response_shape: str  # <-- expected shape for llm response
    llm_type: LLM


class LLMRequestCreate(LLMRequestBase):  # <-- creation data model
    pass


class LLMRequest(LLMRequestBase):
    id: str
    initiated: datetime = datetime.utcnow()

    class Config:
        orm_mode = True
