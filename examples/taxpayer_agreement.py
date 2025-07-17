from fiskaly_sdk import FiskalyClient

client = FiskalyClient(api_key="...", api_secret="...")
client.authenticate()

# Generar acuerdo (borrador)
agreement = client.taxpayer_agreement.generate(content={"language": "es"})
print("Draft agreement:", agreement.content)

# Subir acuerdo firmado (simula estructura real)
upload = client.taxpayer_agreement.upload(content={"file": "<base64pdf>", "filename": "acuerdo.pdf"})
print("Upload status:", upload.content)

# Obtener info del acuerdo
info = client.taxpayer_agreement.get()
print("Agreement info:", info.content)

# Descargar PDF firmado
pdf_bytes = client.taxpayer_agreement.download_pdf()
with open("acuerdo_firmado.pdf", "wb") as f:
    f.write(pdf_bytes)
print("PDF descargado.")
