import os
from loguru import logger

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app.core.interface.service import Service, ServiceFactory

class MySQLService(Service):
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url, pool_size=10, max_overflow=5)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Session = SessionLocal

    def get_session(self) -> sessionmaker:
        return self.Session()

    def set_ready(self):
        logger.info("MySQL is ready")

    def teardown(self):
        logger.info("MySQL is being torn down")
        self.engine.dispose()

class MySQLServiceFactory(ServiceFactory):
    def create(self) -> MySQLService:
        return MySQLService(os.getenv("DATABASE_URL"))