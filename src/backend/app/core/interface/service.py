from abc import ABC, abstractmethod
from typing import Generator
from enum import Enum

class ServiceType(Enum):
    SQLALCHEMY = "sqlalchemy"
    MYSQL = "mysql"
    SQLITE = "sqlite"

class Service(ABC):
    @abstractmethod
    def get_session(self) -> Generator:
        pass

    @abstractmethod
    def set_ready(self):
        pass

    @abstractmethod
    def teardown(self):
        pass

class ServiceFactory(ABC):
    @abstractmethod
    def create(self) -> Service:
        pass

class NoFactoryRegisteredError(Exception):
    pass
