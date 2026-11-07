"""Discretionary DCF Engine: Computes intrinsic value scenario matrices based on macro/micro inputs."""

import numpy as np
import pandas as pd


class ValuationEngine:

  def __init__(
      self, fcf_baseline: float, net_debt: float, shares_outstanding: float
  ):
    """Parameters:

    fcf_baseline: Latest Free Cash Flow (in billions)
    net_debt: Total Debt minus Cash (in billions)
    shares_outstanding: Diluted Shares Outstanding (in billions)
    """
    self.fcf_baseline = fcf_baseline
    self.net_debt = net_debt
    self.shares = shares_outstanding

  def calculate_fair_value(
      self, growth_rate: float, wacc: float, terminal_growth: float = 0.025
  ) -> float:
    """Calculates Fair Value per Share for a single scenario."""
    years = np.arange(1, 6)
    future_fcf = self.fcf_baseline * ((1 + growth_rate) ** years)
    discount_factors = (1 + wacc) ** years
    pv_fcf = np.sum(future_fcf / discount_factors)

    terminal_value = (
        future_fcf[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
    )
    pv_terminal_value = terminal_value / ((1 + wacc) ** 5)

    enterprise_value = pv_fcf + pv_terminal_value
    equity_value = enterprise_value - self.net_debt
    fair_value = equity_value / self.shares

    return round(fair_value, 2)

  def build_sensitivity_matrix(
      self, growth_range: list, wacc_range: list, terminal_growth: float = 0.025
  ) -> pd.DataFrame:
    """Generates a dynamic 2D grid of intrinsic values across discretionary scenarios."""
    matrix = pd.DataFrame(index=growth_range, columns=wacc_range)

    for g in growth_range:
      for w in wacc_range:
        if w > terminal_growth:
          val = self.calculate_fair_value(g, w, terminal_growth)
          matrix.loc[g, w] = f"${val:.2f}"
        else:
          matrix.loc[g, w] = "N/A"

    matrix.index = [f"CAGR: {round(g * 100, 1)}%" for g in matrix.index]
    matrix.columns = [f"WACC: {round(w * 100, 1)}%" for w in matrix.columns]
    return matrix


if __name__ == "__main__":
  # Quick Test: Palantir (PLTR) Approx Baseline Stats
  pltr = ValuationEngine(
      fcf_baseline=4.3, net_debt=-8.0, shares_outstanding=2.4
  )

  growth_scenarios = [0.15, 0.20, 0.25, 0.30, 0.35]
  wacc_scenarios = [0.08, 0.09, 0.10, 0.11, 0.12]

  print("=== PLTR INTRINSIC VALUE MATRIX ===")
  print(pltr.build_sensitivity_matrix(growth_scenarios, wacc_scenarios))
