# examples/advanced_invoicing.py

"""
Ejemplo avanzado: creación, rectificación, enriquecimiento y recuperación de facturas.
"""

from fiskaly_sdk import FiskalyClient

client = FiskalyClient(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET"
)
client.authenticate()

# Supón que ya existe un client_id válido en la organización
client_id = "YOUR_CLIENT_ID"

# Crear factura simple
invoice_content = {
    "invoice_number": "INV-001",
    "issue_date": "2024-07-17",
    # Agrega más campos según tu modelo
}
invoice = client.invoices.create(client_id=client_id, invoice_id=None, content=invoice_content)
print("Factura creada:", invoice.content)

# Buscar facturas de ese client
invoices = client.invoices.search(client_id=client_id)
print("Listado de facturas:", [inv.content for inv in invoices])

# Crear factura rectificativa (correcting)
correcting_content = {
    "original_invoice_id": invoice.content.id,
    "reason": "Corrección de importe"
    # Agrega campos según el modelo
}
corr_invoice = client.invoices.correcting_invoice(client_id, content=correcting_content)
print("Factura rectificativa:", corr_invoice.content)

# Crear enrichment invoice (añadir info a factura existente)
enrichment_content = {
    "invoice_id": invoice.content.id,
    "extra_field": "Valor extra"
}
enr_invoice = client.invoices.enrichment_invoice(client_id, content=enrichment_content)
print("Factura enriquecida:", enr_invoice.content)

# Crear remedy invoice (factura de recuperación)
remedy_content = {
    "invoice_id": invoice.content.id,
    "recovery_reason": "Cliente recuperado"
}
rem_invoice = client.invoices.remedy_invoice(client_id, content=remedy_content)
print("Factura remedy:", rem_invoice.content)

# Cambiar sistema de IVA en una factura
vat_switch_content = {
    "invoice_id": invoice.content.id,
    "vat_type": "special"
}
vat_invoice = client.invoices.vat_system_switch_invoice(client_id, content=vat_switch_content)
print("Factura cambio de IVA:", vat_invoice.content)
