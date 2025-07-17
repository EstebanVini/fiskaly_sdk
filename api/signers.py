# fiskaly_sdk/api/signers.py

"""
API para gestionar firmantes (signers) en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any, List
from ..exceptions import FiskalyApiError
from ..models.signer import (
    SignerRequest,
    SignerStateRequest,
    SignerResponse,
    SignersListResponse,
)
from ..utils import generate_guid

class SignersAPI:
    """
    API para gestionar los dispositivos firmantes (signers).

    Métodos:
      - create(signer_id, metadata)
      - disable(signer_id, metadata)
      - get(signer_id)
      - list()
    """

    def __init__(self, client):
        """
        Inicializa el submódulo signers.

        :param client: Instancia de FiskalyClient.
        """
        self.client = client

    def create(self, signer_id: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> SignerResponse:
        """
        Crea un nuevo signer.

        :param signer_id: GUID único del signer (si None, se genera automáticamente).
        :param metadata: Metadata opcional.
        :return: SignerResponse con datos del signer creado.
        :raises FiskalyApiError: Si la API responde con error.
        """
        signer_id = signer_id or generate_guid()
        body = SignerRequest(metadata=metadata or {})
        resp = self.client.request("PUT", f"/signers/{signer_id}", json=body.dict())
        return SignerResponse.parse_obj(resp)

    def disable(self, signer_id: str, metadata: Optional[Dict[str, Any]] = None) -> SignerResponse:
        """
        Deshabilita (deactiva) un signer existente.

        :param signer_id: ID del signer.
        :param metadata: Metadata adicional (opcional).
        :return: SignerResponse con el nuevo estado.
        :raises FiskalyApiError: Si la API responde con error.
        """
        body = SignerStateRequest(
            content={"state": "DISABLED"},
            metadata=metadata or {}
        )
        resp = self.client.request("PATCH", f"/signers/{signer_id}", json=body.dict())
        return SignerResponse.parse_obj(resp)

    def get(self, signer_id: str) -> SignerResponse:
        """
        Recupera los datos de un signer específico.

        :param signer_id: ID del signer.
        :return: SignerResponse con los datos del signer.
        :raises FiskalyApiError: Si la API responde con error.
        """
        resp = self.client.request("GET", f"/signers/{signer_id}")
        return SignerResponse.parse_obj(resp)

    def list(self) -> List[SignerResponse]:
        """
        Lista todos los signers de la organización.

        :return: Lista de SignerResponse para cada signer.
        :raises FiskalyApiError: Si la API responde con error.
        """
        resp = self.client.request("GET", "/signers")
        list_response = SignersListResponse.parse_obj(resp)
        return [SignerResponse(content=item) for item in list_response.content]
