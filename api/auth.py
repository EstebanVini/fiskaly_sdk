# fiskaly_sdk/api/auth.py

"""
Módulo para autenticación y obtención de Bearer Token con la API Fiskaly SIGN ES.
"""

from typing import Optional
from ..exceptions import FiskalyAuthError
from ..models.auth import AuthRequest, AuthResponse

class AuthAPI:
    """
    API de autenticación Fiskaly.

    Permite obtener y refrescar el token Bearer para realizar operaciones protegidas.
    """

    def __init__(self, client):
        """
        Inicializa el módulo de autenticación.

        :param client: Instancia de FiskalyClient.
        """
        self.client = client

    def retrieve_access_token(self) -> str:
        """
        Solicita un token Bearer usando las credenciales configuradas en el cliente.

        :return: Token Bearer válido para ser usado en llamadas autenticadas.
        :raises FiskalyAuthError: Si la autenticación falla.
        """
        # Prepara payload (puedes usar AuthRequest si quieres validación extra)
        payload = {
            "content": {
                "api_key": self.client.config.api_key,
                "api_secret": self.client.config.api_secret
            }
        }
        try:
            # Usa el método centralizado para facilitar los mocks y la trazabilidad
            response = self.client.request(
                method="POST",
                endpoint="/auth",
                json=payload
            )
        except Exception as e:
            raise FiskalyAuthError(f"Error de conexión al autenticar: {e}")

        try:
            # Aquí podrías validar con Pydantic v2 (model_validate)
            auth_response = AuthResponse.model_validate(response)
            bearer = auth_response.content.access_token.bearer
            self.client.set_bearer_token(bearer)
            return bearer
        except Exception as e:
            raise FiskalyAuthError(f"Error procesando la respuesta de autenticación: {e}")
