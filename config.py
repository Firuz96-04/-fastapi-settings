from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    host: str = "localhost"
    port: int = 5001
    reload: bool = True
    password: str = 'password'
    some: str = 'test'


settings= Settings()