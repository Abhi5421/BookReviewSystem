from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv(verbose=True)


class Setting(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    SQLALCHEMY_DATABASE_URL: str


settings = Setting()