from typing import Generator
from loguru import logger

import mysql.connector

from app.core.interface.service import Service, ServiceFactory
from app.core.config import settings

class MySQLService(Service):
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=settings.MYSQL_HOST,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASSWORD,
            database=settings.MYSQL_DB
        )

    def get_session(self) -> Generator[mysql.connector.connection_cext.CMySQLConnection, None, None]:
        try:
            yield self.connection
        finally:
            self.connection.close()

    def set_ready(self):
        logger.info("MySQLService is ready")

    def teardown(self):
        logger.info("MySQLService is being torn down")
        self.connection.close()

class MySQLServiceFactory(ServiceFactory):
    def create(self) -> MySQLService:
        return MySQLService()
