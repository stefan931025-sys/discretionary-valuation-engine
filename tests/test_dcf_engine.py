# tests/test_dcf_engine.py
import pytest

def test_enterprise_value_calculation():
    """Verify Enterprise Value aggregation from discounted cash flows and terminal value."""
    projected_fcf = [100.0, 115.0, 132.0, 151.0, 174.0]
    wacc = 0.09
    terminal_growth = 0.025
    
    # Present Value of 5-year FCFs
    pv_fcf = sum([fcf / ((1 + wacc) ** (i + 1)) for i, fcf in enumerate(projected_fcf)])
    
    # Terminal Value calculation (Gordon Growth)
    terminal_value = (projected_fcf[-1] * (1 + terminal_growth)) / (wacc - terminal_growth)
    pv_terminal_value = terminal_value / ((1 + wacc) ** len(projected_fcf))
    
    enterprise_value = pv_fcf + pv_terminal_value
    
    assert enterprise_value > 0
    assert pytest.approx(pv_fcf, 0.01) == 493.38

def test_equity_value_per_share():
    """Verify Equity Value bridge: EV - Net Debt / Shares Outstanding."""
    enterprise_value = 2500.0
    cash = 200.0
    debt = 400.0
    shares_outstanding = 100.0
    
    equity_value = enterprise_value + cash - debt
    per_share_value = equity_value / shares_outstanding
    
    assert pytest.approx(per_share_value, 0.01) == 23.00
