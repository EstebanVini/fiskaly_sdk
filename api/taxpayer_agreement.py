from ..models.taxpayer_agreement import (
    TaxpayerAgreementGenerateRequest,
    TaxpayerAgreementUploadRequest,
    TaxpayerAgreementResponse,
)

class TaxpayerAgreementAPI:
    """
    API para la gestión del acuerdo del taxpayer (contribuyente).
    """
    def __init__(self, client):
        self.client = client

    def generate(self, content) -> TaxpayerAgreementResponse:
        """
        Genera el borrador del acuerdo.
        """
        body = TaxpayerAgreementGenerateRequest(content=content)
        resp = self.client.request("POST", "/taxpayer/agreement", json=body.dict())
        return TaxpayerAgreementResponse.model_validate(resp)

    def upload(self, content) -> TaxpayerAgreementResponse:
        """
        Sube el acuerdo firmado.
        """
        body = TaxpayerAgreementUploadRequest(content=content)
        resp = self.client.request("PUT", "/taxpayer/agreement", json=body.dict())
        return TaxpayerAgreementResponse.model_validate(resp)

    def get(self) -> TaxpayerAgreementResponse:
        """
        Obtiene la información del acuerdo del taxpayer.
        """
        resp = self.client.request("GET", "/taxpayer/agreement")
        return TaxpayerAgreementResponse.model_validate(resp)

    def download_pdf(self) -> bytes:
        """
        Descarga el PDF del acuerdo firmado.
        """
        resp = self.client.request("GET", "/taxpayer/agreement.pdf")
        return resp  # bytes
