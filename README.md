
# Fiskaly SIGN ES Python SDK (Unofficial)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fiskaly-sdk-sign-es)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-orange.svg)]()

Unofficial Python SDK for easy integration with the [Fiskaly SIGN ES](https://www.fiskaly.com/es/) API.  
Developed and maintained by Esteban Viniegra Pérez Olagaray.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Resources](#api-resources)
- [Configuration](#configuration)
- [Examples](#examples)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

---

## Introduction

**Fiskaly SIGN ES Python SDK** is an unofficial implementation to interact with the Fiskaly SIGN ES API.  
It simplifies tasks such as managing taxpayers, clients, invoices, signers, agreements, exports, and more—handling authentication, request/response models, and data validation in a Pythonic way.

---

## Features

- **Full client for Fiskaly SIGN ES API**  
- **Strongly-typed request and response models** with Pydantic
- **Handles authentication** (API Key/Secret)
- Endpoints for:
  - Taxpayers
  - Clients
  - Invoices (create, search)
  - Signers
  - Exports
  - Software info
  - Taxpayer Agreements
- **Async-ready structure** (add your own async logic if needed)
- **Easy configuration**
- **Custom error handling**

---

## Installation

```bash
pip install git+https://github.com/EstebanVini/fiskaly_sdk.git
```

or clone and install locally:

```bash
git clone https://github.com/EstebanVini/fiskaly_sdk.git
cd fiskaly_sdk
pip install .
```

> **Python 3.7+ required**

---

## Usage

### Basic Example

```python
from fiskaly_sdk.client import FiskalyClient

# Initialize the client with your credentials
client = FiskalyClient(
    api_key="your_fiskaly_api_key",
    api_secret="your_fiskaly_api_secret"
)

# Example: Create a taxpayer
taxpayer_data = {
    # Fill with required taxpayer fields according to Fiskaly's API
}
response = client.taxpayer.create(taxpayer_data)
print(response)
```

### Authentication

The client manages authentication using the API Key and Secret.  
Tokens are handled internally, but you can access authentication endpoints if needed.

---

## API Resources

The SDK supports all main SIGN ES resources, each with corresponding Python methods and Pydantic models.

| Resource             | Methods Available (via FiskalyClient) |
|----------------------|---------------------------------------|
| **Auth**             | Authenticate, refresh token           |
| **Taxpayers**        | Create, update, retrieve, state       |
| **Clients**          | Register, update, retrieve, state     |
| **Invoices**         | Create, retrieve, search              |
| **Signers**          | Register, manage, retrieve            |
| **Exports**          | Create, update, retrieve              |
| **Software**         | Retrieve software info                |
| **TaxpayerAgreement**| Generate, upload, retrieve            |
| **Invoice XML/Search** | Generate invoice XML, search invoices|

**All API methods return strongly-typed Pydantic model instances for safe and easy data access.**

---

## Configuration

Configuration is done via the `FiskalyClient` constructor:

```python
client = FiskalyClient(
    api_key="your_api_key",
    api_secret="your_api_secret",
    base_url="https://sign-api.fiskaly.com/api/v1",  # optional, default provided
    timeout=30,                                      # optional, in seconds
    verify_ssl=True                                  # optional, for SSL verification
)
```

For advanced scenarios, refer to the `fiskaly_sdk/config.py` file for more options.

---

## Examples

### Creating an Invoice

```python
invoice_data = {
    # Required fields per API model
}
invoice_response = client.invoices.create(invoice_data)
print(invoice_response)
```

### Fetching a List of Clients

```python
clients = client.clients.list(page=1, page_size=10)
for cl in clients:
    print(cl.id, cl.name)
```

### Error Handling

```python
from fiskaly_sdk.exceptions import FiskalyApiError

try:
    client.invoices.create(invalid_data)
except FiskalyApiError as e:
    print(f"API Error: {e}")
```

---

## Dependencies

- [requests](https://pypi.org/project/requests/) >= 2.25.1
- [pydantic](https://pypi.org/project/pydantic/) >= 2.0.0

Install automatically via `pip`.

---

## Troubleshooting

- **Authentication errors:** Check your API key/secret and permissions.
- **Validation errors:** Ensure request data matches the expected Pydantic models.
- **Timeouts/connection errors:** Check your network and base URL.
- **API changes:** This SDK is unofficial; monitor upstream Fiskaly API updates.

---

## Contributors

- **Esteban Viniegra Pérez Olagaray**  
  [esteban@eviniegra.software](mailto:esteban@eviniegra.software)

Feel free to submit pull requests or issues!

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Disclaimer

> This SDK is an **unofficial** implementation and not affiliated with Fiskaly.  
> Use at your own risk. For production deployments, always validate functionality against the latest Fiskaly SIGN ES API documentation.

---
