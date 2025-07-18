from fiskaly_sdk import FiskalyClient

client = FiskalyClient(api_key="...", api_secret="...")
client.authenticate()

xml_bytes = client.invoice_xml.get_xml(client_id="client1", invoice_id="inv123")
with open("factura.xml", "wb") as f:
    f.write(xml_bytes)
print("Factura XML exportada.")
