# fiskaly_sdk/models/software.py

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class SoftwareResponseContent(BaseModel):
    software_id: str = Field(..., description="ID del software")
    name: str = Field(..., description="Nombre del software")
    # Puedes agregar más campos según lo que devuelve la API

class SoftwareResponse(BaseModel):
    content: SoftwareResponseContent
    metadata: Optional[Dict[str, Any]] = None
