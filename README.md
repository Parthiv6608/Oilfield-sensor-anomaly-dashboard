# Oilfield Sensor Anomaly Dashboard

## Overview

This project is a Python-based dashboard for analyzing simulated oilfield equipment sensor data. It detects abnormal patterns in pressure, temperature, vibration, and flow-rate readings and converts them into maintenance alerts.

The goal is to demonstrate how software, data analytics, and anomaly detection can support industrial operations in oil and gas environments.

## Problem

Oilfield equipment such as pumps, compressors, wellheads, and pipelines can generate continuous sensor data. Abnormal patterns in this data may indicate equipment stress, possible failure, production issues, or maintenance needs.

If these patterns are missed, they can lead to downtime, safety risks, and inefficient operations.

## Solution

This dashboard will load sensor data, analyze trends, detect abnormal readings, and generate simple maintenance recommendations.

The first version will use rule-based anomaly detection. Later versions may include machine learning models such as Isolation Forest.

## Features

- Load simulated oilfield sensor data from CSV
- Track pressure, temperature, vibration, and flow rate
- Detect abnormal sensor readings
- Display equipment-level risk status
- Generate maintenance alerts
- Visualize sensor trends in an interactive dashboard

## Tech Stack

- Python
- Pandas
- NumPy
- Streamlit
- Plotly
- scikit-learn

## Project Structure

```text
oilfield-sensor-anomaly-dashboard/
│
├── data/
│   └── sample_sensor_data.csv
│
├── src/
│   ├── generate_sample_data.py
│   ├── data_loader.py
│   ├── anomaly_detector.py
│   ├── maintenance_report.py
│   └── dashboard.py
│
├── docs/
│   ├── project_log.md
│   └── design_notes.md
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
