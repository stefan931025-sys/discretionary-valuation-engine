# Discretionary Asset Valuation & Stock Pitch Engine

[![CI Pipeline](https://github.com/stefan931025-sys/discretionary-valuation-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/stefan931025-sys/discretionary-valuation-engine/actions/workflows/ci.yml)

![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview

This repository contains a quantitative decision-support tool designed for active discretionary portfolio management and institutional stock selection. By decoupling static price targets from traditional Discounted Cash Flow (DCF) models, this engine provides a dynamic Sensitivity Matrix allowing discretionary traders to evaluate intrinsic stock valuations across varying macroeconomic (WACC / discount rates) and microeconomic (revenue CAGR) scenario combinations.

## Key Features

* **Dynamic Scenario Modelling:** Python engine calculating Enterprise Value and Equity Value per share based on customizable 5-year Free Cash Flow trajectories.
* **Macro & Micro Stress-Testing:** Instant 2D matrix output for evaluating intrinsic value sensitivity across varying interest rate environments and growth assumptions.
* **Institutional Stock Pitch Suite:** Modular trade proposals incorporating fundamental trade catalysts, asymmetric risk/reward setups, target prices, and stop-loss levels.

## Repository Structure

```text
discretionary-valuation-engine/
├── requirements.txt      # System dependencies (numpy, pandas)
├── .gitignore            # Python runtime ignore rules
├── src/
│   └── dcf_engine.py     # Dynamic DCF scenario calculator
└── pitches/
    ├── PLTR_valuation_memo.md # Palantir Technologies pitch memo & matrix
    └── NDAQ_valuation_memo.md # Nasdaq Inc pitch memo & matrix
