from typing import List, Optional
from uuid import UUID
from fastapi import HTTPException
from sqlmodel import Session, select

from app.service.processing.model import Processing
from app.api.v1.schemas.processing import ProcessingCreate, ProcessingUpdate

class ProcessingService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_processings(self, user_id: Optional[UUID] = None, processing_type: Optional[str] = None):
        statement = select(Processing)
        if user_id:
            statement = statement.where(Processing.user_id == user_id)
        if processing_type:
            statement = statement.where(Processing.processing_type == processing_type)
        return self.session.exec(statement).all()

    def create_processing(self, processing_data: ProcessingCreate):
        try:
            new_processing = Processing(**processing_data.model_dump())
            self.session.add(new_processing)
            self.session.commit()
            self.session.refresh(new_processing)
            return new_processing
        except Exception as e:
            raise e

    def update_processing(self, processing_id: UUID, processing_update: ProcessingUpdate):
        try:
            processing = self.session.get(Processing, processing_id)
            if not processing:
                raise HTTPException(status_code=404, detail="Processing not found")
            for key, value in processing_update.model_dump(exclude_unset=True).items():
                setattr(processing, key, value)
            self.session.add(processing)
            self.session.commit()
            self.session.refresh(processing)
            return processing
        except Exception as e:
            raise e

    def delete_processing(self, processing_id: UUID):
        try:
            processing = self.session.get(Processing, processing_id)
            if not processing:
                raise HTTPException(status_code=404, detail="Processing not found")
            self.session.delete(processing)
            self.session.commit()
        except Exception as e:
            raise e
