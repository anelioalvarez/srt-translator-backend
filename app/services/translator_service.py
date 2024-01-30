from fastapi import Depends
from app.configs.environment import EnvironmentSettings, get_env_settings
from srt import Subtitle
import srt
from typing import List
from deep_translator import GoogleTranslator
import detectlanguage


class TranslatorService:
    env_settings: EnvironmentSettings

    def __init__(
        self,
        env_settings: EnvironmentSettings = Depends(get_env_settings)
    ) -> None:
        self.env_settings = env_settings

    def parse_srt(self, text_file: str) -> List[Subtitle]:
        subs = srt.parse(text_file)
        return list(subs)

    def get_supported_languages(self):
        langs = GoogleTranslator().get_supported_languages(as_dict=True)
        return langs

    def detect_language(self, text_file: str):
        detectlanguage.configuration.api_key = self.env_settings.DETECT_LANGUAGE_API_KEY
        lang = detectlanguage.detect(text_file)

        return lang
