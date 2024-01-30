from fastapi import FastAPI
from app.routers.translator_router import TranslatorRouter


app = FastAPI()

app.include_router(TranslatorRouter)
