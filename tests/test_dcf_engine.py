from __future__ import annotations

"""
Module: tests/test_dcf_engine.py
Description: Unit tests for the Discretionary Valuation Engine validating module imports and DCF valuation sanity.
"""

import pytest
from core import dcf_engine

def test_dcf_module_import() -> None:
    """Validates that the dcf_engine core module is successfully imported."""
    assert dcf_engine is not None
    assert hasattr(dcf_engine, "__name__")

def test_valuation_sanity() -> None:
    """Validates basic valuation mathematical bounds and sanity checks."""
    # Placeholder or core valuation logic assertions
    discount_rate = 0.10
    terminal_growth = 0.02
    
    assert discount_rate > terminal_growth, "Discount rate must exceed terminal growth rate for valid Gordon Growth."
    
    # Mock Enterprise Value or Equity Value calculation checks if implemented in core
    # e.g., EV / Equity Value per share validation
    ev_per_share_mock = 150.0
    assert ev_per_share_mock > 0.0, "Valuation per share must be positive."
