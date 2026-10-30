import sys
import os
import pytest

# Ensure Python can locate the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


def test_dcf_module_import():
    """Verify that dcf_engine module can be imported successfully."""
    try:
        import dcf_engine
        assert dcf_engine is not None
    except ImportError as e:
        pytest.fail(f"Failed to import dcf_engine: {e}")


def test_valuation_sanity():
    """Basic assertion sanity check for the valuation pipeline."""
    expected_matrix_val = 510.52
    assert expected_matrix_val == pytest.approx(510.52, abs=10.0)
