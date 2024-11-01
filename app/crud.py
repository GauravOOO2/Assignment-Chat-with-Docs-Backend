# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def create_document(db: Session, document: schemas.DocumentCreate):
    db_document = models.Document(
        filename=document.filename,
        document_metadata=document.document_metadata,
        content=document.content
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def create_user(email: str, name: str):
    db_user = models.User(email=email, name=name)  # Create a User model
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(email: str):
    return db.query(models.User).filter(models.User.email == email).first()
