"""Helper para crear un SparkSession con configuración amigable para local/Windows."""
from __future__ import annotations

import os
import sys

from pyspark.sql import SparkSession


def _ensure_pyspark_python() -> None:
    """En Windows el alias de Microsoft Store de `python` rompe los workers.

    PySpark lanza procesos `python` adicionales por cada worker; si en el PATH
    aparece primero el alias de Microsoft Store, esos workers cuelgan o fallan.
    Apuntamos PYSPARK_PYTHON al intérprete real (el que está corriendo este código).
    """
    if not os.environ.get("PYSPARK_PYTHON"):
        os.environ["PYSPARK_PYTHON"] = sys.executable
    if not os.environ.get("PYSPARK_DRIVER_PYTHON"):
        os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable


def get_spark(app_name: str = "drifting-minsky") -> SparkSession:
    _ensure_pyspark_python()
    return (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "4")
        .config("spark.driver.memory", "1g")
        .config("spark.ui.showConsoleProgress", "false")
        .getOrCreate()
    )
