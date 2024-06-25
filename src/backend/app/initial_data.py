import json
from pathlib import Path
from sqlmodel import Session, select, delete
from uuid import UUID

from app.service.provider.model import Provider
from app.service.model.model import Model
from app.service.credential.model import Credential
from app.service.store.model import Store
from app.service.store.service import StoreService
from app.api.v1.schemas.store import StoreCreate
from app.service.processing.model import Processing
from app.service.agent.model import Agent


def init_db(session: Session):
    provider_data_path = Path("./app/data/provider_data.json")
    model_data_path = Path("./app/data/model_data.json")
    credential_data_path = Path("./app/data/credential_data.json")
    processing_data_path = Path("./app/data/processing_data.json")
    agent_data_path = Path("./app/data/agent_data.json")    

    provider_data = json.loads(provider_data_path.read_text())
    model_data = json.loads(model_data_path.read_text())
    credential_data = json.loads(credential_data_path.read_text())
    processing_data = json.loads(processing_data_path.read_text())
    agent_data = json.loads(agent_data_path.read_text())

    clear_provider_table(session)

    statement = select(Provider)
    results = session.exec(statement)
    if not results.first():
        providers = [Provider(**data) for data in provider_data]
        session.add_all(providers)
        session.commit()

    create_model_data(session, model_data)
    create_credential_data(session, credential_data)
    create_store_data(session)
    create_processing_data(session, processing_data)
    create_agent_data(session, agent_data)

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

def create_credential_data(session: Session, model_data):

    clear_credential_table(session)
    models = []
    for data in model_data:
        provider_name = data.pop("credential_name")
        provider = session.exec(select(Provider).where(Provider.name == provider_name)).first()
        if provider:
            provider_id = provider.provider_id

        data["provider_id"] = provider_id
        data["credential_name"] = 'Default '+provider_name
        models.append(Credential(**data))

    session.add_all(models)
    session.commit()

def clear_credential_table(session: Session):
    statement = delete(Credential)
    session.exec(statement)
    session.commit()

def create_store_data(session: Session):

    clear_store_table(session)

    store_data = StoreCreate(
        store_name="Default Storage",
        description="Default Storage with Cloudwiz AI FMOps",
        creator_id=UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
        updater_id=UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
        user_id=UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6")
    )
    service = StoreService(session)
    service.create_store(store_data)

def clear_store_table(session: Session):
    service = StoreService(session)
    statement = select(Store)
    stores = session.exec(statement).all()
    for store in stores:
        service.delete_store(store.store_id)

def create_processing_data(session: Session, processing_data):

    clear_processing_table(session)

    statement = select(Processing)
    results = session.exec(statement)
    if not results.first():
        processing = [Processing(**data) for data in processing_data]
        session.add_all(processing)
        session.commit()

def clear_processing_table(session: Session):
    statement = delete(Processing)
    session.exec(statement)
    session.commit()

def create_agent_data(session: Session, agent_data):
    agents = []
    # for data in agent_data:
    #     provider_name = data.pop("credential_name")
    #     provider = session.exec(select(Agent).where(Provider.name == provider_name)).first()
    #     if provider:
    #         provider_id = provider.provider_id

    #     data["provider_id"] = provider_id

    #     agents.append(Agent(**data))

    # session.add_all(agents)
    # session.commit()    