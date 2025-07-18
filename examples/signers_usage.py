# examples/signers_usage.py

"""
Ejemplo de gestión de signers (dispositivos firmantes) en el SDK Fiskaly SIGN ES.
"""

from fiskaly_sdk import FiskalyClient

client = FiskalyClient(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET"
)
client.authenticate()

# Crear un signer (si no envías ID, se genera uno aleatorio)
signer = client.signers.create(metadata={"device": "Caja 1"})
print("Signer creado:", signer.content)

# Listar todos los signers
signers_list = client.signers.list()
print("Signers en la organización:")
for s in signers_list:
    print(f"  - {s.content.id} (estado: {s.content.state})")

# Obtener datos de un signer específico
signer_id = signer.content.id
signer_info = client.signers.get(signer_id)
print("Info del signer:", signer_info.content)

# Deshabilitar un signer
disable_resp = client.signers.disable(signer_id)
print("Signer deshabilitado:", disable_resp.content)
