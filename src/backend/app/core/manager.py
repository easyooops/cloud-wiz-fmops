from typing import Dict
from loguru import logger

from app.core.interface.service import NoFactoryRegisteredError, Service, ServiceFactory, ServiceType
from app.core.provider.database.SQLAlchemy import SQLAlchemyServiceFactory
from app.core.provider.database.MySQL import MySQLServiceFactory
from app.core.provider.database.SQLite import SQLiteServiceFactory

class ServiceManager:
    def __init__(self):
        self.services: Dict[str, Service] = {}
        self.factories: Dict[ServiceType, ServiceFactory] = self._initialize_factories()

    def _initialize_factories(self) -> Dict[ServiceType, ServiceFactory]:
        return {
            ServiceType.SQLALCHEMY: SQLAlchemyServiceFactory(),
            ServiceType.MYSQL: MySQLServiceFactory(),
            ServiceType.SQLITE: SQLiteServiceFactory()
        }

    def get_service(self, service_type: ServiceType) -> Service:
        if service_type not in self.services:
            self._create_service(service_type)
        return self.services[service_type.value]

    def _create_service(self, service_type: ServiceType):
        factory = self.factories.get(service_type)
        if not factory:
            raise NoFactoryRegisteredError(f"No factory registered for {service_type.name}")
        self.services[service_type.value] = factory.create()
        self.services[service_type.value].set_ready()

    def teardown_services(self):
        for service in self.services.values():
            if service:
                logger.debug(f"Teardown service {service.__class__.__name__}")
                service.teardown()
        self.services = {}
