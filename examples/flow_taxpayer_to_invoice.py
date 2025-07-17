# examples/flow_taxpayer_to_invoice.py

"""
Ejemplo de flujo completo: alta de taxpayer, signer, client y emisión de factura.
"""

from fiskaly_sdk import FiskalyClient

client = FiskalyClient(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET"
)
client.authenticate()

# Paso 1: Alta de taxpayer (emisor)
taxpayer_resp = client.taxpayer.set(
    issuer_tax_number="B12345678",
    issuer_legal_name="Empresa Demo S.L.",
    territory="GIPUZKOA"
)
print("Taxpayer registrado:", taxpayer_resp.content)

# Paso 2: Alta de signer (firmante)
signer_resp = client.signers.create(metadata={"device": "Caja Central"})
signer_id = signer_resp.content.id
print("Signer creado:", signer_resp.content)

# Paso 3: Alta de client (TPV/dispositivo)
client_resp = client.clients.create(metadata={"tpv": "TPV 01"})
client_id = client_resp.content.id
print("Client creado:", client_resp.content)

# Paso 4: Emisión de factura
invoice_content = {
    "invoice_number": "INV-1001",
    "issue_date": "2024-07-17"
    # Agrega el resto de campos requeridos según tu modelo
}
invoice_resp = client.invoices.create(client_id=client_id, invoice_id=None, content=invoice_content)
print("Factura emitida:", invoice_resp.content)
