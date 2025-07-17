# fiskaly_sdk/api/taxpayer_agreement.py

from typing import Dict, Any, Optional
from ..models.taxpayer_agreement import (
    TaxpayerAgreementGenerateRequest,
    TaxpayerAgreementUploadRequest,
    TaxpayerAgreementResponse,
)
from ..exceptions import FiskalyApiError

class TaxpayerAgreementAPI:
    """
    API para la gestión del acuerdo del taxpayer (contribuyente).
    """
    def __init__(self, client):
        self.client = client

    def generate(self, content: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, Any]] = None) -> TaxpayerAgreementResponse:
        """
        Genera el borrador del acuerdo.
        """
        body = TaxpayerAgreementGenerateRequest(content=content or {}, metadata=metadata or {})
        resp = self.client.request("POST", "/taxpayer/agreement", json=body.dict())
        return TaxpayerAgreementResponse.parse_obj(resp)

    def upload(self, content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> TaxpayerAgreementResponse:
        """
        Sube el acuerdo firmado.
        """
        body = TaxpayerAgreementUploadRequest(content=content, metadata=metadata or {})
        resp = self.client.request("PUT", "/taxpayer/agreement", json=body.dict())
        return TaxpayerAgreementResponse.parse_obj(resp)

    def get(self) -> TaxpayerAgreementResponse:
        """
        Obtiene la información del acuerdo del taxpayer.
        """
        resp = self.client.request("GET", "/taxpayer/agreement")
        return TaxpayerAgreementResponse.parse_obj(resp)

    def download_pdf(self) -> bytes:
        """
        Descarga el PDF del acuerdo firmado.
        """
        resp = self.client.request("GET", "/taxpayer/agreement.pdf")
        return resp  # bytes
