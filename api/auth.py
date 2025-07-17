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
        # Prepara payload
        payload = {
            "content": {
                "api_key": self.client.config.api_key,
                "api_secret": self.client.config.api_secret
            }
        }
        try:
            response = self.client.session.post(
                url=f"{self.client.config.base_url}/auth",
                json=payload,
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                timeout=self.client.config.timeout
            )
        except Exception as e:
            raise FiskalyAuthError(f"Error de conexión al autenticar: {e}")

        if response.status_code != 200:
            try:
                err = response.json()
            except Exception:
                err = response.text
            raise FiskalyAuthError(f"Error autenticando: {err}")

        try:
            auth_response = AuthResponse.parse_obj(response.json())
            bearer = auth_response.content.access_token.bearer
            self.client.set_bearer_token(bearer)
            return bearer
        except Exception as e:
            raise FiskalyAuthError(f"Error procesando la respuesta de autenticación: {e}")
