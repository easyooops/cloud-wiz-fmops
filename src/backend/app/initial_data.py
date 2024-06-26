import json
from pathlib import Path
import uuid
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

    clear_abent_table(session)

    agents = []
    for data in agent_data:

        fm_provider = session.exec(select(Provider).where(Provider.name == "OpenAI")).first()

        if not validate_uuid(fm_provider.provider_id):
            print(fm_provider.provider_id)
            return
        data["fm_provider_id"] = fm_provider.provider_id
        data["embedding_provider_id"] = fm_provider.provider_id

        model_typ = data.pop("fm_provider_type")
        model_name = None
        if model_typ == "C":
            model_name = "gpt-3.5-turbo"
        elif model_typ == "T":
            model_name = "gpt-3.5-turbo-instruct"

        fm_model = session.exec(select(Model).where(Model.model_name == model_name)).first()
        if not validate_uuid(fm_model.model_id):
            print(fm_model.model_id)
            return
        data["fm_provider_type"] = model_typ
        data["fm_model_id"] = fm_model.model_id


        embedding_model = session.exec(select(Model).where(Model.model_name == "text-embedding-ada-002")).first()
        if not validate_uuid(embedding_model.model_id):
            print(embedding_model.model_id)
            return        
        data["embedding_model_id"] = embedding_model.model_id

        store_provider = session.exec(select(Provider).where(Provider.name == "Amazon S3")).first()
        if not validate_uuid(store_provider.provider_id):
            print(store_provider.provider_id)
            return          
        data["storage_provider_id"] = store_provider.provider_id

        object_name = session.exec(select(Store).where(Store.store_name == "Default Storage")).first()
        if not validate_uuid(object_name.store_id):
            print(object_name.store_id)
            return                
        data["storage_object_id"] = object_name.store_id

        pre_processing = session.exec(select(Processing).where(Processing.processing_type == "pre")).first()
        if not validate_uuid(pre_processing.processing_id):
            print(pre_processing.processing_id)
            return          
        data["pre_processing_id"] = pre_processing.processing_id

        post_processing = session.exec(select(Processing).where(Processing.processing_type == "post")).first()
        if not validate_uuid(post_processing.processing_id):
            print(post_processing.processing_id)
            return                
        data["post_processing_id"] = post_processing.processing_id

        data["vector_db_provider_id"] = None

        agents.append(Agent(**data))

    session.add_all(agents)
    session.commit()

def clear_abent_table(session: Session):
    statement = delete(Agent)
    session.exec(statement)
    session.commit()

def validate_uuid(value):
    if isinstance(value, uuid.UUID):
        return True
    try:
        uuid_obj = uuid.UUID(value)
        return True
    except ValueError:
        return False  