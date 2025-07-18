# fiskaly_sdk/__init__.py

"""
Módulo principal del SDK Fiskaly SIGN ES para Python.

Provee el cliente principal y la versión del SDK.
"""

from .client import FiskalyClient
from .version import __version__

__all__ = [
    "FiskalyClient",
    "__version__"
]
