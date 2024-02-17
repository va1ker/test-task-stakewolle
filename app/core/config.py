import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 3600
    REDIS_URL: str = "redis://redis:6379/0"
    REDIS_HOST:str = 'redis' 
    REDIS_PORT:str ="6379" 
    REDIS_DB:str = "0"
    DATABASE_ECHO:bool = True
    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgres@postgres:5432/stakewolle"
    )
    model_config = SettingsConfigDict(
        env_file=".env",
    )


class TestConfig(Config):
    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgres@postgres:5432/stakewolle_test"
    )


class LocalConfig(Config): ...


class ProductionConfig(Config):
    DEBUG: bool = False


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "test": TestConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
        "development": Config(),
    }
    return config_type[env]


config: Config = get_config()
