# fiskaly_sdk/models/export.py

"""
Modelos de datos para el recurso Exports en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field

class ExportRequestContent(BaseModel):
    """
    Modelo para el contenido de la solicitud de exportación de facturas.
    """
    # Puedes definir filtros de exportación según OpenAPI o Postman (fecha, estado, etc.)
    # Aquí se usa un dict flexible.
    pass

class ExportRequest(BaseModel):
    """
    Modelo de request para crear una exportación.
    """
    content: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExportUpdateRequest(BaseModel):
    """
    Modelo para actualizar metadata de la exportación.
    """
    content: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExportResponseContent(BaseModel):
    """
    Contenido de la respuesta de una exportación.
    """
    id: str = Field(..., description="ID único de la exportación")
    state: Optional[str] = None
    # Agrega más campos según lo que devuelva la API

class ExportResponse(BaseModel):
    """
    Modelo de respuesta de una exportación.
    """
    content: ExportResponseContent
    metadata: Optional[Dict[str, Any]] = None

class ExportsListResponse(BaseModel):
    """
    Modelo para la respuesta de listado de exportaciones.
    """
    content: List[ExportResponseContent]
