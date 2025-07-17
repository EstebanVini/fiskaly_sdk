# fiskaly_sdk/models/taxpayer_agreement.py

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class TaxpayerAgreementGenerateRequest(BaseModel):
    content: Dict[str, Any] = Field(default_factory=dict)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class TaxpayerAgreementUploadRequest(BaseModel):
    content: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class TaxpayerAgreementResponseContent(BaseModel):
    agreement_id: str = Field(..., description="ID del acuerdo")
    state: str = Field(..., description="Estado del acuerdo")

class TaxpayerAgreementResponse(BaseModel):
    content: TaxpayerAgreementResponseContent
    metadata: Optional[Dict[str, Any]] = None
