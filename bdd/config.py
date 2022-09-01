from pydantic import BaseSettings, HttpUrl


class Settings(BaseSettings):
    base_url: HttpUrl

    class Config:
        env_file = '.env'
        env_nested_delimiter = '__'


settings = Settings()
