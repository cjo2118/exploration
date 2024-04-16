from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import src.explore.models
import src.explore.crud
from src.explore.api.schemas import LLMRequestCreate
from src.explore.database import SessionLocal, engine

from src.explorefwrk import logger

log = logger.get_logger(__name__)

src.explore.models.Base.metadata.create_all(bind=engine)

# Router basic information
router = APIRouter(
    prefix="/explore",
    tags=["Chat"],
    responses={404: {"description": "Not found"}}
)


# Dependency: Used to get the database in our endpoints.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/llm-request", response_model=src.explore.api.schemas.LLMRequest)
async def create_llm_request(create_request: LLMRequestCreate, db: Session = Depends(get_db)):
    """
    Create a new llm request
    """
    log.info(f"Creating llm request")
    log.info(create_request)
    request = src.explore.crud.create_llm_request(db, create_request)
    log.info(f"Created llm request")
    return request


# Root endpoint for the router.
@router.get("/")
async def explore_root():
    return {"message": "Hello there conversational ai!"}
