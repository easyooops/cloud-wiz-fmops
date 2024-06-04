from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.service.agent.service import AgentService
from app.api.v1.schemas.agent import AgentCreate, AgentUpdate
from app.core.exception import internal_server_error
from app.service.agent.model import Agent

router = APIRouter()

@router.get("/", response_model=List[Agent])
def get_agents(
    type: Optional[str] = None,
    name: Optional[str] = None,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = AgentService(session)
        return service.get_all_agents(type, name)
    except Exception as e:
        raise internal_server_error(e)

@router.post("/", response_model=Agent)
def create_agent(
    agent: AgentCreate, 
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = AgentService(session)
        return service.create_agent(agent)
    except Exception as e:
        raise internal_server_error(e)

@router.put("/{agent_id}", response_model=Agent)
def update_agent(
    agent_id: int,
    agent_update: AgentUpdate,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = AgentService(session)
        return service.update_agent(agent_id, agent_update)
    except Exception as e:
        raise internal_server_error(e)

@router.delete("/{agent_id}")
def delete_agent(
    agent_id: int,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = AgentService(session)
        service.delete_agent(agent_id)
        return {"message": "Agent deleted successfully"}
    except Exception as e:
        raise internal_server_error(e)
