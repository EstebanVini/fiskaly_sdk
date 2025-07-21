from pydantic import BaseModel, Field
from typing import Optional, List, Dict

# -- BillingOptions (puede ir en otro archivo si quieres)
class BillingOptions(BaseModel):
    gln: Optional[str] = Field(None, description="Global Location Number")
    withhold_billing: Optional[bool] = Field(None, description="Only true if bill_to_organization is provided/set")
    bill_to_organization: Optional[str] = Field(None, description="UUID of the billed organization")

# -- Organization Model (para creación)
class Organization(BaseModel):
    name: str
    address_line1: str
    zip: str
    town: str
    country_code: str
    display_name: Optional[str]
    vat_id: Optional[str]
    contact_person_id: Optional[str]
    address_line2: Optional[str]
    state: Optional[str]
    tax_number: Optional[str]
    economy_id: Optional[str]
    billing_options: Optional[BillingOptions]
    billing_address_id: Optional[str]
    metadata: Optional[Dict[str, str]]
    managed_by_organization_id: str


# -- Organization Response
class OrganizationResponse(Organization):
    _id: str
    _type: str
    _envs: List[str]
    managed_by_organization_id: Optional[str]
    managed_configuration: Optional[Dict]
    created_by_user: Optional[str]

class ListOrganizationsResponse(BaseModel):
    data: List[OrganizationResponse]
    count: int
    _type: str
