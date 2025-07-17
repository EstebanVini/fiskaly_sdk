# API Reference

> Documentación de referencia para el SDK Fiskaly SIGN ES en Python.

---

## Índice

- [FiskalyClient](#fiskalyclient)
- [Recursos principales](#recursos-principales)
    - [Autenticación (`auth`)](#autenticación-auth)
    - [Taxpayer (`taxpayer`)](#taxpayer-taxpayer)
    - [Taxpayer Agreement (`taxpayer_agreement`)](#taxpayer_agreement-taxpayer_agreement)
    - [Signers (`signers`)](#signers-signers)
    - [Clients (`clients`)](#clients-clients)
    - [Invoices (`invoices`)](#invoices-invoices)
    - [Exports (`exports`)](#exports-exports)
    - [Invoice XML (`invoice_xml`)](#invoice_xml-invoice_xml)
    - [Global Invoice Search (`invoice_search`)](#invoice_search-invoice_search)
    - [Software (`software`)](#software-software)
- [Excepciones principales](#excepciones-principales)
- [Validación de datos](#validación-de-datos)
- [Más información](#más-información)

---

## FiskalyClient

Clase principal. Punto de entrada del SDK.

```python
from fiskaly_sdk import FiskalyClient

client = FiskalyClient(
    api_key="...",
    api_secret="..."
)
client.authenticate()