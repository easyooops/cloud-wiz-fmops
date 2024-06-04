from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str

    SQLALCHEMY_DATABASE_URL: str

    # AWS
    COGNITO_REGION: str

    # MySQL
    MYSQL_HOST: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str

    class Config:
        env_file = ".app.env"

settings = Settings()