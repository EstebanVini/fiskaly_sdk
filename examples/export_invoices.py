# examples/export_invoices.py

"""
Ejemplo de exportación de facturas y descarga de archivo ZIP.
"""

from fiskaly_sdk import FiskalyClient

client = FiskalyClient(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET"
)
client.authenticate()

# Crear exportación
export_content = {
    # Agrega filtros, por ejemplo rango de fechas, estados, etc.
    "from_date": "2024-01-01",
    "to_date": "2024-07-17"
}
export = client.exports.create(content=export_content)
print("Exportación iniciada:", export.content.id)

# Descargar el ZIP asociado (cuando esté listo en la API)
zip_bytes = client.exports.download_zip(export.content.id)
with open("invoices_export.zip", "wb") as f:
    f.write(zip_bytes)
print("Archivo ZIP guardado como invoices_export.zip")
