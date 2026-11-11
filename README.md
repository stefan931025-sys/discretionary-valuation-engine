# Discretionary Asset Valuation & Stock Pitch Engine

[![Discretionary Asset Valuation CI](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/stefan931025-sys/discretionary-valuation-engine)
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A quantitative decision-support tool designed for active discretionary portfolio management and institutional stock selection, featuring dynamic DCF sensitivity matrices and modular investment memos.

---

## Overview & Methodology

This engine decouples static price targets from traditional Discounted Cash Flow (DCF) models, providing a dynamic sensitivity matrix that allows discretionary traders to evaluate intrinsic stock valuations across varying macroeconomic ($\text{WACC}$ / discount rates) and microeconomic (revenue $\text{CAGR}$) scenario combinations.

---

## Key Features

* **Dynamic Scenario Modelling:** Python engine calculating Enterprise Value and Equity Value per share based on customizable 5-year Free Cash Flow trajectories.
* **Macro & Micro Stress-Testing:** Instant 2D matrix output for evaluating intrinsic value sensitivity across varying interest rate environments and growth assumptions.
* **Institutional Stock Pitch Suite:** Modular trade proposals incorporating fundamental trade catalysts, asymmetric risk/reward setups, target prices, and stop-loss levels (located in `pitches/`).

---

## Mathematical Specifications

### 1. Enterprise Value via Discounted Free Cash Flows
$$\text{EV} = \sum_{t=1}^{5} \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{FCFF}_5 (1 + g)}{(\text{WACC} - g)(1 + \text{WACC})^5}$$

### 2. Equity Value Per Share
$$\text{Value per Share} = \frac{\text{EV} - \text{Total Debt} + \text{Cash}}{\text{Diluted Shares Outstanding}}$$

---

## System Architecture & Data Flow

```text
+-----------------------------------------------------------------------------------+
|                     MACROECONOMIC & FUNDAMENTAL ASSUMPTIONS                       |
|           (WACC Ranges, Revenue Growth CAGR, Margins, & Terminal Rates)           |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                         DYNAMIC DCF SENSITIVITY ENGINE                            |
|  * 5-Year FCFF Projection Matrix              * Gordon Growth Terminal Calculation|
|  * 2D WACC vs. Growth Sensitivity Grids       * Implied Share Price Surface       |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                        DISCRETIONARY PITCH & DECISION DESK                        |
|             (Asymmetric Risk/Reward Profiles, Target Prices, & Memos)             |
+-----------------------------------------------------------------------------------+
