
from sqlmodel import Session
from typing import Generator, Optional

from app.core.manager import ServiceManager
from app.core.interface.service import ServiceType

service_manager = ServiceManager()

def get_database(service_type: Optional[ServiceType] = None) -> Generator[Session, None, None]:

    if service_type == None:
        # service_type = ServiceType.SQLALCHEMY
        service_type = ServiceType.MYSQL
        # service_type = ServiceType.SQLITE

    db_service = service_manager.get_service(service_type)
    db = db_service.get_session()

    try:
        yield db
    finally:
        db.close()