"""
Modelos de datos para el recurso Taxpayer (contribuyente/emisor) en el SDK Fiskaly SIGN ES.
"""

from pydantic import BaseModel, Field

class IssuerModel(BaseModel):
    """
    Representa la información del emisor (taxpayer).
    """
    tax_number: str = Field(..., description="Número de identificación fiscal del emisor")
    legal_name: str = Field(..., description="Nombre legal del emisor")

class TaxpayerRequestContent(BaseModel):
    """
    Modelo del campo 'content' para las operaciones de creación/actualización de taxpayer.
    """
    issuer: IssuerModel
    territory: str = Field(..., description="Territorio (ej: GIPUZKOA)")

class TaxpayerRequest(BaseModel):
    """
    Modelo completo de request para set taxpayer.
    """
    content: TaxpayerRequestContent
    metadata: dict | None = Field(default=None, description="Metadatos adicionales para el taxpayer")

class TaxpayerStateRequest(BaseModel):
    """
    Modelo de request para deshabilitar taxpayer.
    """
    content: dict = Field(..., description="Estado a establecer, p.ej: {'state': 'DISABLED'}")

class TaxpayerResponseContent(BaseModel):
    """
    Modelo del campo 'content' en la respuesta de taxpayer.
    """
    issuer: IssuerModel
    territory: str
    state: str

class TaxpayerResponse(BaseModel):
    """
    Modelo completo de response para taxpayer.
    """
    content: TaxpayerResponseContent
