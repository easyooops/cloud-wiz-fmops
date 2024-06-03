
from sqlmodel import Session
from typing import Generator

from app.core.manager import ServiceManager
from app.core.interface.service import ServiceType

service_manager = ServiceManager()

def get_database(service_type: ServiceType) -> Generator[Session, None, None]:
    db_service = service_manager.get_service(service_type)
    db = db_service.get_session()
    try:
        yield db
    finally:
        db.close()