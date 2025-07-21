"""
API para gestionar firmantes (signers) en el SDK Fiskaly SIGN ES.
"""

from typing import Optional, Dict, Any
from ..exceptions import FiskalyApiError
from ..models.signer import (
    SignerStateRequest,
    SignerModel,
    SignersListResponse
)
from ..utils import generate_guid

class SignersAPI:
    """
    API para gestionar los dispositivos firmantes (signers).

    Métodos:
      - create(signer_id, metadata, certificate_b64, private_key_b64, private_key_password)
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

    def create(
        self,
        signer_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        certificate_b64: Optional[str] = None,
        private_key_b64: Optional[str] = None,
        private_key_password: Optional[str] = None,
    ) -> SignerModel:
        """
        Crea un nuevo signer. Si se pasan certificado y clave, se suben a la API.

        :param signer_id: ID único del signer (opcional).
        :param metadata: Metadata adicional (opcional).
        :param certificate_b64: Certificado X509 en base64 (opcional).
        :param private_key_b64: Clave privada en base64 (opcional, obligatorio si se pasa certificate).
        :param private_key_password: Password de la clave privada (opcional).
        :return: SignerModel
        :raises FiskalyApiError: Si la API responde con error.
        """
        signer_id = signer_id or generate_guid()
        body = {"metadata": metadata or {}}

        if certificate_b64 and private_key_b64:
            content = {
                "certificate": certificate_b64,
                "private_key": private_key_b64,
            }
            if private_key_password:
                content["private_key_password"] = private_key_password
            body["content"] = content

        resp = self.client.request("PUT", f"/signers/{signer_id}", json=body)
        return SignerModel.model_validate(resp)

    def disable(self, signer_id: str, metadata: Optional[Dict[str, Any]] = None) -> SignerModel:
        """
        Deshabilita (deactiva) un signer existente.

        :param signer_id: ID del signer.
        :param metadata: Metadata adicional (opcional).
        :return: SignerModel con el nuevo estado.
        :raises FiskalyApiError: Si la API responde con error.
        """
        body = SignerStateRequest(
            content={"state": "DISABLED"},
            metadata=metadata or {}
        )
        resp = self.client.request("PATCH", f"/signers/{signer_id}", json=body.dict())
        return SignerModel.model_validate(resp)

    def get(self, signer_id: str) -> SignerModel:
        """
        Recupera los datos de un signer específico.

        :param signer_id: ID del signer.
        :return: SignerModel con los datos del signer.
        :raises FiskalyApiError: Si la API responde con error.
        """
        resp = self.client.request("GET", f"/signers/{signer_id}")
        return SignerModel.model_validate(resp)

    def list(self) -> SignersListResponse:
        """
        Lista todos los signers de la organización.

        :return: SignersListResponse con los signers y la paginación.
        :raises FiskalyApiError: Si la API responde con error.
        """
        resp = self.client.request("GET", "/signers")
        return SignersListResponse.model_validate(resp)
