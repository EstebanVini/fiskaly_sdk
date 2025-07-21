# fiskaly_sdk/api/__init__.py

"""
Submódulo API del SDK Fiskaly SIGN ES.

Incluye los clientes para interactuar con todos los recursos de la API:
    - AuthAPI
    - TaxpayerAPI
    - SignersAPI
    - ClientsAPI
    - InvoicesAPI
    - ExportsAPI
    - TaxpayerAgreementAPI
    - InvoiceXMLAPI
    - InvoiceSearchAPI
    - SoftwareAPI
"""

from .auth import AuthAPI
from .taxpayer import TaxpayerAPI
from .signers import SignersAPI
from .clients import ClientsAPI
from .invoices import InvoicesAPI
from .exports import ExportsAPI
from .taxpayer_agreement import TaxpayerAgreementAPI
from .invoice_xml import InvoiceXMLAPI
from .invoice_search import InvoiceSearchAPI
from .software import SoftwareAPI
from .management_auth import ManagementAuthAPI  # Importa el nuevo módulo de autenticación administrativa   
from .organizations import OrganizationsAPI  # Importa el nuevo módulo de organizaciones
