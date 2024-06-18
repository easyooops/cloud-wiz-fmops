import json
from pathlib import Path
from sqlmodel import Session, select, delete
from uuid import UUID

from app.service.provider.model import Provider
from app.service.model.model import Model

def init_db(session: Session):
    provider_data_path = Path("./app/data/provider_data.json")
    model_data_path = Path("./app/data/model_data.json")

    provider_data = json.loads(provider_data_path.read_text())
    model_data = json.loads(model_data_path.read_text())

    clear_provider_table(session)

    statement = select(Provider)
    results = session.exec(statement)
    if not results.first():
        providers = [Provider(**data) for data in provider_data]
        session.add_all(providers)
        session.commit()

    create_model_data(session, model_data)

def clear_provider_table(session: Session):
    statement = delete(Provider)
    session.exec(statement)
    session.commit()

def create_model_data(session: Session, model_data):

    clear_model_table(session)
    models = []
    for data in model_data:
        provider_name = data.pop("provider_name")
        provider = session.exec(select(Provider).where(Provider.name == provider_name)).first()
        if provider:
            provider_id = provider.provider_id

        data["provider_id"] = provider_id
        models.append(Model(**data))

    session.add_all(models)
    session.commit()

def clear_model_table(session: Session):
    statement = delete(Model)
    session.exec(statement)
    session.commit()    