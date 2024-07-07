
from sqlmodel import Session
from typing import Generator

from app.core.manager import ServiceManager
from app.core.interface.service import ServiceType

service_manager = ServiceManager()

def get_database() -> Generator[Session, None, None]:

    service_type = ServiceType.SQLALCHEMY
    # service_type = ServiceType.MYSQL
    # service_type = ServiceType.SQLITE

    db_service = service_manager.get_service(service_type)
    db = db_service.get_session()
    try:
        yield db
    finally:
        db.close()