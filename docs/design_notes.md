# Design Notes

## Project Purpose

This project is designed to simulate how industrial sensor data can be used to monitor oilfield equipment and detect abnormal behavior.

The project focuses on four types of sensor readings:

- Pressure
- Temperature
- Vibration
- Flow rate

## Simulated Equipment

The first version of the project will use simulated data for:

- Pump-01
- Compressor-02
- Wellhead-03
- Pipeline-04

## Anomaly Examples

The simulated dataset will include normal readings as well as abnormal events such as:

- Sudden pressure increases
- Rising equipment temperature
- Vibration spikes
- Flow-rate drops

## Detection Strategy

The first version will use simple rule-based anomaly detection.

Examples:

- Pressure is flagged if it is far above normal range
- Temperature is flagged if it rises sharply
- Vibration is flagged if it spikes suddenly
- Flow rate is flagged if it drops unexpectedly

Later versions may include machine learning methods such as Isolation Forest.