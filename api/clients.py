# fiskaly_sdk/api/clients.py

"""
API para gestionar dispositivos cliente (clients) en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any, List
from ..exceptions import FiskalyApiError
from ..models.client import (
    ClientRequest,
    ClientStateRequest,
    ClientResponse,
    ClientsListResponse,
)
from ..utils import generate_guid

class ClientsAPI:
    """
    API para gestionar los dispositivos cliente (clients).

    Métodos:
      - create(client_id, metadata)
      - disable(client_id, metadata)
      - get(client_id)
      - list()
    """

    def __init__(self, client):
        """
        Inicializa el submódulo clients.

        :param client: Instancia de FiskalyClient.
        """
        self.client = client

    def create(self, client_id: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> ClientResponse:
        """
        Crea un nuevo client.

        :param client_id: GUID único del client (si None, se genera automáticamente).
        :param metadata: Metadata opcional.
        :return: ClientResponse con los datos del client creado.
        :raises FiskalyApiError: Si la API responde con error.
        """
        client_id = client_id or generate_guid()
        body = ClientRequest(metadata=metadata or {})
        resp = self.client.request("PUT", f"/clients/{client_id}", json=body.dict())
        return ClientResponse.model_validate(resp)

    def disable(self, client_id: str, metadata: Optional[Dict[str, Any]] = None) -> ClientResponse:
        """
        Deshabilita (deactiva) un client existente.

        :param client_id: ID del client.
        :param metadata: Metadata adicional (opcional).
        :return: ClientResponse con el nuevo estado.
        :raises FiskalyApiError: Si la API responde con error.
        """
        body = ClientStateRequest(
            content={"state": "DISABLED"},
            metadata=metadata or {}
        )
        resp = self.client.request("PATCH", f"/clients/{client_id}", json=body.dict())
        return ClientResponse.model_validate(resp)

    def get(self, client_id: str) -> ClientResponse:
        """
        Recupera los datos de un client específico.

        :param client_id: ID del client.
        :return: ClientResponse con los datos del client.
        :raises FiskalyApiError: Si la API responde con error.
        """
        resp = self.client.request("GET", f"/clients/{client_id}")
        return ClientResponse.model_validate(resp)

    def list(self, limit: int = 10, token: Optional[str] = None) -> ClientsListResponse:
        """
        Lista todos los clients de la organización, soportando paginación.

        :param limit: Límite de elementos por página.
        :param token: Token de paginación (si aplica).
        :return: ClientsListResponse con la lista paginada de clientes.
        :raises FiskalyApiError: Si la API responde con error.
        """
        params = {"limit": limit}
        if token:
            params["token"] = token
        resp = self.client.request("GET", "/clients", params=params)
        return ClientsListResponse.model_validate(resp)
