"""
Modelos de datos para el recurso Clients en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field

class ClientRequestContent(BaseModel):
    """
    Modelo para el contenido del request de creación/actualización de client.
    """
    # El endpoint realmente solo usa metadata, pero puede crecer a futuro.
    pass

class ClientRequest(BaseModel):
    """
    Modelo completo de request para crear/actualizar un client.
    """
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ClientStateRequest(BaseModel):
    """
    Modelo para deshabilitar (PATCH) un client.
    """
    content: Dict[str, str] = Field(..., description="Estado a establecer, p.ej: {'state': 'DISABLED'}")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ClientSignerModel(BaseModel):
    """
    Modelo para el signer anidado dentro de un client.
    """
    id: str = Field(..., description="ID del signer asociado a este client")

class ClientResponseContent(BaseModel):
    """
    Contenido de la respuesta al obtener datos de un client.
    """
    id: str = Field(..., description="ID único del client (device_id)")
    signer: ClientSignerModel
    state: Optional[str] = None

class ClientResponse(BaseModel):
    """
    Modelo completo de response para client.
    """
    content: ClientResponseContent
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ClientsPaginationModel(BaseModel):
    """
    Modelo para la paginación de la respuesta de listado de clients.
    """
    limit: int
    next: Optional[str] = None
    token: Optional[str] = None

class ClientsListResponse(BaseModel):
    """
    Modelo para la respuesta de listado de clients.
    """
    pagination: ClientsPaginationModel
    results: List[ClientResponse]
