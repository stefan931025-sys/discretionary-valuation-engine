# Discretionary Asset Valuation & Stock Pitch Engine

![CI Workflow](https://github.com/stefan931025-sys/discretionary-valuation-engine/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A quantitative decision-support tool designed for active discretionary portfolio management and institutional stock selection, featuring dynamic DCF sensitivity matrices and modular investment memos[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).

## 🚀 Overview & Methodology

This engine decouples static price targets from traditional Discounted Cash Flow (DCF) models, providing a dynamic sensitivity matrix that allows discretionary traders to evaluate intrinsic stock valuations across varying macroeconomic (WACC / discount rates) and microeconomic (revenue CAGR) scenario combinations[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span).

## 🔑 Key Features

* **Dynamic Scenario Modelling:** Python engine calculating Enterprise Value and Equity Value per share based on customizable 5-year Free Cash Flow trajectories[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).
* **Macro & Micro Stress-Testing:** Instant 2D matrix output for evaluating intrinsic value sensitivity across varying interest rate environments and growth assumptions[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span).
* **Institutional Stock Pitch Suite:** Modular trade proposals incorporating fundamental trade catalysts, asymmetric risk/reward setups, target prices, and stop-loss levels (located in `pitches/`)[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span).

---

## 📊 Mathematical Specifications

### 1. Enterprise Value via Discounted Free Cash Flows

$$\text{EV} = \sum_{t=1}^{5} \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{FCFF}_5 (1 + g)}{(\text{WACC} - g)(1 + \text{WACC})^5}$$

### 2. Equity Value Per Share

$$\text{Value per Share} = \frac{\text{EV} - \text{Total Debt} + \text{Cash}}{\text{Diluted Shares Outstanding}}$$

---

## 📁 Repository Structure

```text
discretionary-valuation-engine/
├── .devcontainer/             # Devcontainer configuration for Codespaces[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span)
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions automated test workflow[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span)
├── core/
│   └── dcf_engine.py          # DCF valuation & scenario matrix modules[span_20](start_span)[span_20](end_span)[span_21](start_span)[span_21](end_span)
├── pitches/                   # Institutional stock pitch Markdown memos[span_22](start_span)[span_22](end_span)[span_23](start_span)[span_23](end_span)
├── tests/
│   └── test_dcf_engine.py     # Automated pytest suite[span_24](start_span)[span_24](end_span)[span_25](start_span)[span_25](end_span)
├── main.py                    # Main execution pipeline script[span_26](start_span)[span_26](end_span)[span_27](start_span)[span_27](end_span)
├── repo_auditor.py            # Static AST analysis governance tool[span_28](start_span)[span_28](end_span)[span_29](start_span)[span_29](end_span)
├── requirements.txt           # Python dependencies[span_30](start_span)[span_30](end_span)[span_31](start_span)[span_31](end_span)
└── README.md                  # System documentation[span_32](start_span)[span_32](end_span)[span_33](start_span)[span_33](end_span)
