# fiskaly_sdk/api/management_auth.py

"""
Módulo para autenticación y obtención de Bearer Token con la API Fiskaly SIGN ES.
"""
from requests import Session
from typing import Optional

import requests
from ..exceptions import FiskalyAuthError
from ..models.management_auth import *

class ManagementAuthAPI:
    """
    API de autenticación Administrativa de Fiskaly.

    Permite obtener y refrescar el token Bearer para realizar operaciones protegidas.
    """

    def __init__(self, client):
        """
        Inicializa el módulo de autenticación.

        :param client: Instancia de FiskalyClient.
        """
        self.client = client

    def retrieve_management_access_token(self) -> str:
        """
        Solicita un token Bearer usando las credenciales configuradas en el cliente.

        :return: Token Bearer válido para ser usado en llamadas autenticadas.
        :raises FiskalyAuthError: Si la autenticación falla.
        """
        # URL de administración
        management_url = "https://dashboard.fiskaly.com/api/v0"
        # Prepara payload (puedes usar AuthRequest si quieres validación extra)
        payload = {
            "api_key": self.client.config.management_api_key,
            "api_secret": self.client.config.management_api_secret
        }
        try:
            #No Usa el método centralizado, hace el request directamente a la url de administración
            response = self.client.session.post(
                f"{management_url}/auth",
                json=payload,
            )
            response.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        except requests.exceptions.HTTPError as http_err:
            raise FiskalyAuthError(f"Error HTTP al autenticar: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            raise FiskalyAuthError(f"Error de conexión al autenticar: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            raise FiskalyAuthError(f"Timeout al autenticar: {timeout_err}")
        except Exception as e:
            raise FiskalyAuthError(f"Error de conexión al autenticar: {e}")
        try:
            # OJO: Primero deserializa la respuesta a dict
            data = response.json()
            auth_response = ManagementAuthResponse.model_validate(data)
            bearer = auth_response.access_token
            organization_id = auth_response.access_token_claims.organization_id
            self.client.set_management_bearer_token(bearer)
            self.client.set_organization_id(organization_id)
            return bearer, organization_id
        except ValueError as e:
            raise FiskalyAuthError(f"Error de validación de la respuesta de autenticación: {e}")
        except Exception as e:
            raise FiskalyAuthError(f"Error procesando la respuesta de autenticación: {e}")