from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    SQLALCHEMY_DATABASE_URL: str

    # MySQL
    MYSQL_HOST: str = ""
    MYSQL_USER: str = ""
    MYSQL_PASSWORD: str = ""
    MYSQL_DB: str = ""

    class Config:
        env_file = ".app.env"

settings = Settings()