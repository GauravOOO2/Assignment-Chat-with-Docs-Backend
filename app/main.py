# app/main.py
from fastapi import FastAPI, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from .config import settings
from . import models, schemas, crud, utils, nlp, auth
from .database import SessionLocal, engine
import os

# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the auth router
app.include_router(auth.router)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload_document", response_model=schemas.DocumentResponse)
async def upload_document(file: UploadFile, db: Session = Depends(get_db)):
    try:
        # Save the file to a temporary location
        temp_file_path = os.path.join(os.getcwd(), file.filename)
        with open(temp_file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)

        # Parse document
        parsed_content, document_metadata = utils.parse_document(temp_file_path)

        # Clean up temporary file
        os.remove(temp_file_path)

        # Save parsed data to PostgreSQL
        document_data = schemas.DocumentCreate(
            filename=file.filename,
            document_metadata=document_metadata,
            content=parsed_content
        )
        db_document = crud.create_document(db=db, document=document_data)

        # Index the document for NLP processing
        nlp.index_document(db_document)

        return db_document
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@app.get("/query")
async def query_documents(user_query: str, db: Session = Depends(get_db)):
    try:
        response = nlp.query_documents(user_query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error querying documents: {str(e)}")