# Market Deviation Tracker

A lightweight Python utility that detects short-term price deviations in commodity markets and triggers alerts when thresholds are exceeded.

This project demonstrates **anomaly detection, threshold-based alerting, and signal vs noise reasoning**, using real market data.

## What This Demonstrates

- Python data ingestion and processing
- Basic anomaly detection using percentage change
- Clear decision logic (alert vs no alert)
- Translating raw data into actionable signals

This mirrors how alerts are generated and evaluated in security operations and monitoring systems.

## How It Works

1. Pulls recent price data using Yahoo Finance (via `yfinance`)
2. Calculates day-over-day percentage change
3. Compares change against a defined threshold
4. Outputs an alert when a deviation is detected

## Example Use Case

- Detect abnormal price movements caused by supply shocks
- Demonstrate alert logic similar to SOC detections
- Prototype decision thresholds before automation

## Repository Structure

```text
market-deviation-tracker/
├── README.md
├── market_deviation_tracker.py
├── requirements.txt
├── idea/
│   └── initial-notes.md
├── legacy_versions/
│   └── previous-iterations.py
└── CHANGELOG.md
