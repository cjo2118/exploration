from fastapi import FastAPI

from src.explorefwrk.logger import setup_applevel_logger
from src.explore.api.routes import router as ai_explorer

log = setup_applevel_logger(file_name='explore.log')

app = FastAPI()
app.include_router(router=ai_explorer)


@app.get("/")
async def root():
    return {"message": "Hello there conversational ai user!"}
