from fastapi import APIRouter, UploadFile, Depends
from typing import Dict


from app.services.translator_service import TranslatorService


TranslatorRouter = APIRouter(
    prefix="/translator",
    tags=["translator"]
)


@TranslatorRouter.post("/")
async def parse_file(
    upload_file: UploadFile,
    translator_service: TranslatorService = Depends()
):
    file = await upload_file.read()
    subs = translator_service.parse_srt(file.decode())

    return subs


@TranslatorRouter.get("/supported-languages")
async def get_supported_languages(
    translator_service: TranslatorService = Depends()
) -> Dict[str, str]:
    langs = translator_service.get_supported_languages()

    return langs


@TranslatorRouter.post("/detect-language")
async def detect_language(
    upload_file: UploadFile,
    translator_service: TranslatorService = Depends()
):
    file = await upload_file.read()
    lang = translator_service.detect_language(file.decode())

    return lang
