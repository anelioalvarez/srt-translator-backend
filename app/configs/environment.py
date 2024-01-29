from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


@lru_cache
def get_env_filename():
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):
    DETECT_LANGUAGE_API_KEY: str

    model_config = SettingsConfigDict(env_file=get_env_filename())


@lru_cache
def get_env_settings():
    return EnvironmentSettings()
