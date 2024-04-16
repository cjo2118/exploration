import uuid
from sqlalchemy.orm import Session
from src.explore import models
from src.explore.api import schemas


def create_llm_request(db: Session, llm_request: schemas.LLMRequestCreate):
    """
    Create llm request record in our database
    """
    db_llm_request = models.LLMRequest(
        id=str(uuid.uuid4()),
        input=llm_request.input,
        response_shape=llm_request.response_shape,
        llm_type=llm_type_to_db_enum(llm_request.llm_type)
    )
    db.add(db_llm_request)
    db.commit()
    db.refresh(db_llm_request)

    return db_llm_request


def llm_type_to_db_enum(llm_type: schemas.LLM) -> str:
    # dangerous, should use if/else
    if llm_type.GPT_35:
        return "gpt-3.5"
    elif llm_type.GPT_4:
        return "gpt-4"
    else:
        return "gpt-3.5"
