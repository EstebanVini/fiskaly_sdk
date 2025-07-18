# fiskaly_sdk/models/invoice.py

"""
Modelos de datos para el recurso Invoices (facturas) y casos especiales en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field

class InvoiceRequest(BaseModel):
    content: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class InvoiceResponseContent(BaseModel):
    id: str = Field(..., description="ID único de la factura")
    state: Optional[str]

class InvoiceResponse(BaseModel):
    content: InvoiceResponseContent
    metadata: Optional[Dict[str, Any]] = None

class PaginationModel(BaseModel):
    limit: int
    next: Optional[str] = None
    token: Optional[str] = None

class InvoicesListResponse(BaseModel):
    results: List[InvoiceResponse]
    pagination: Optional[PaginationModel] = None
