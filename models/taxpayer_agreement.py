from pydantic import BaseModel, Field

# Puedes modelar Address en detalle según el OpenAPI, aquí un placeholder:
class AddressModel(BaseModel):
    street: str
    city: str
    postal_code: str
    country: str

class RepresentativeModel(BaseModel):
    full_name: str
    tax_number: str
    address: AddressModel

class TaxpayerAgreementGenerateRequestContent(BaseModel):
    representative: RepresentativeModel

class TaxpayerAgreementGenerateRequest(BaseModel):
    content: TaxpayerAgreementGenerateRequestContent

class TaxpayerAgreementUploadRequest(BaseModel):
    content: dict

class TaxpayerAgreementResponseContent(BaseModel):
    agreement_id: str = Field(..., description="ID del acuerdo")
    state: str = Field(..., description="Estado del acuerdo")

class TaxpayerAgreementResponse(BaseModel):
    content: TaxpayerAgreementResponseContent
