# fiskaly_sdk/logging_config.py

"""
Configuración centralizada de logging para el SDK Fiskaly.
"""

import logging

def setup_logging(level=logging.INFO):
    """
    Configura el logging global del SDK Fiskaly.

    :param level: Nivel de logging (por defecto: INFO).
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    logging.getLogger("fiskaly_sdk").setLevel(level)
