from pydantic import BaseSettings, HttpUrl, BaseModel


class Auth(BaseModel):
    api_key: str
    api_secret: str
    otp: int


class Settings(BaseSettings):
    base_url: HttpUrl
    auth: Auth

    class Config:
        env_file = '.env'
        env_nested_delimiter = '__'


settings = Settings()
