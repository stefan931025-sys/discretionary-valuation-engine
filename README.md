# Discretionary Asset Valuation & Stock Pitch Engine

![CI Workflow](https://github.com/stefan931025-sys/discretionary-valuation-engine/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A quantitative decision-support tool designed for active discretionary portfolio management and institutional stock selection, featuring dynamic DCF sensitivity matrices and modular investment memos.

## 🚀 Overview & Methodology

This engine decouples static price targets from traditional Discounted Cash Flow (DCF) models, providing a dynamic sensitivity matrix that allows discretionary traders to evaluate intrinsic stock valuations across varying macroeconomic (WACC / discount rates) and microeconomic (revenue CAGR) scenario combinations.

## 🔑 Key Features

* **Dynamic Scenario Modelling:** Python engine calculating Enterprise Value and Equity Value per share based on customizable 5-year Free Cash Flow trajectories.
* **Macro & Micro Stress-Testing:** Instant 2D matrix output for evaluating intrinsic value sensitivity across varying interest rate environments and growth assumptions.
* **Institutional Stock Pitch Suite:** Modular trade proposals incorporating fundamental trade catalysts, asymmetric risk/reward setups, target prices, and stop-loss levels (located in `pitches/`).

---

## 📊 Mathematical Specifications

### 1. Enterprise Value via Discounted Free Cash Flows

$$\text{EV} = \sum_{t=1}^{5} \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{FCFF}_5(1 + g)}{(\text{WACC} - g)(1 + \text{WACC})^5}$$

### 2. Equity Value Per Share

$$\text{Value per Share} = \frac{\text{EV} - \text{Total Debt} + \text{Cash}}{\text{Diluted Shares Outstanding}}$$

---

## 📁 Repository Structure

```text
discretionary-valuation-engine/
├── .devcontainer/     # Devcontainer configuration for Codespaces
├── .github/
│   └── workflows/
│       └── ci.yml     # GitHub Actions automated test workflow
├── core/
│   └── dcf_engine.py  # DCF valuation & scenario matrix modules
├── pitches/           # Institutional stock pitch Markdown memos
├── tests/
│   └── test_dcf_engine.py # Automated pytest suite
├── main.py            # Main execution pipeline script
├── repo_auditor.py    # Static AST analysis governance tool
├── requirements.txt   # Python dependencies
└── README.md          # System documentation
