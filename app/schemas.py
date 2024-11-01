from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class DocumentCreate(BaseModel):
    filename: str
    document_metadata: dict
    content: str

class DocumentResponse(DocumentCreate):
    id: int
    upload_date: datetime
    embeddings: Optional[List[float]]  # Include embeddings if needed
