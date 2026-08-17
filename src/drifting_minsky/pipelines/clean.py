"""Limpieza de datos crudos del pipeline."""
from __future__ import annotations


def is_valid_quantity(quantity: int | None) -> bool:
    """Una cantidad de pedido es válida solo si existe y es mayor que cero.

    Resuelve el issue #1: descartamos cantidades nulas o <= 0.
    """
    return quantity is not None and quantity > 0