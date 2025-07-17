# fiskaly_sdk/models/auth.py

"""
Modelos de datos para la autenticación en el SDK Fiskaly SIGN ES.
"""

from pydantic import BaseModel, Field

class AuthRequestContent(BaseModel):
    """
    Contenido necesario para solicitar un token de acceso (api_key y api_secret).
    """
    api_key: str = Field(..., description="API Key proporcionada por Fiskaly")
    api_secret: str = Field(..., description="API Secret proporcionado por Fiskaly")

class AuthRequest(BaseModel):
    """
    Modelo de request completo para autenticación.
    """
    content: AuthRequestContent

class AuthToken(BaseModel):
    """
    Modelo para el token de autenticación devuelto por Fiskaly.
    """
    bearer: str = Field(..., description="Token Bearer para autenticación en la API")
    expires_at: int = Field(..., description="Timestamp (segundos) de expiración del token")

class AuthResponseContent(BaseModel):
    """
    Modelo de contenido de la respuesta de autenticación.
    """
    access_token: AuthToken

class AuthResponse(BaseModel):
    """
    Modelo de respuesta completa para autenticación.
    """
    content: AuthResponseContent
