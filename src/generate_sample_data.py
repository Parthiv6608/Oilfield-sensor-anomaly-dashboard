from pathlib import Path
import numpy as np
import pandas as pd


def generate_sensor_data() -> pd.DataFrame:
    """
    Generate simulated sensor data for oilfield equipment.

    The dataset includes normal operating behavior and a few injected anomaly events.
    These anomalies will later be used to test the anomaly detection logic.
    """

    rng = np.random.default_rng(seed=42)

    # 48 hours of readings, one reading every 5 minutes
    timestamps = pd.date_range(
        start="2026-01-01 00:00:00",
        periods=48 * 12,
        freq="5min",
    )

    equipment_profiles = {
        "Pump-01": {
            "pressure": 210,
            "temperature": 72,
            "vibration": 0.35,
            "flow_rate": 520,
        },
        "Compressor-02": {
            "pressure": 330,
            "temperature": 88,
            "vibration": 0.55,
            "flow_rate": 430,
        },
        "Wellhead-03": {
            "pressure": 480,
            "temperature": 65,
            "vibration": 0.25,
            "flow_rate": 610,
        },
        "Pipeline-04": {
            "pressure": 260,
            "temperature": 58,
            "vibration": 0.20,
            "flow_rate": 760,
        },
    }

    all_rows = []

    for equipment_id, profile in equipment_profiles.items():
        n = len(timestamps)

        pressure = rng.normal(profile["pressure"], 8, n)
        temperature = rng.normal(profile["temperature"], 3, n)
        vibration = rng.normal(profile["vibration"], 0.04, n)
        flow_rate = rng.normal(profile["flow_rate"], 15, n)

        is_anomaly = np.zeros(n, dtype=bool)
        anomaly_type = np.array(["normal"] * n, dtype=object)

        # Inject equipment-specific abnormal events
        if equipment_id == "Pump-01":
            # Vibration spike
            vibration[180:210] += 0.45
            is_anomaly[180:210] = True
            anomaly_type[180:210] = "vibration_spike"

        elif equipment_id == "Compressor-02":
            # Sustained temperature increase
            temperature[260:320] += np.linspace(8, 25, 60)
            is_anomaly[260:320] = True
            anomaly_type[260:320] = "temperature_rise"

        elif equipment_id == "Wellhead-03":
            # Sudden pressure increase
            pressure[120:145] += 90
            is_anomaly[120:145] = True
            anomaly_type[120:145] = "pressure_spike"

        elif equipment_id == "Pipeline-04":
            # Flow rate drop
            flow_rate[390:430] -= 180
            is_anomaly[390:430] = True
            anomaly_type[390:430] = "flow_rate_drop"

        equipment_data = pd.DataFrame(
            {
                "timestamp": timestamps,
                "equipment_id": equipment_id,
                "pressure": pressure.round(2),
                "temperature": temperature.round(2),
                "vibration": vibration.round(3),
                "flow_rate": flow_rate.round(2),
                "is_anomaly": is_anomaly,
                "anomaly_type": anomaly_type,
            }
        )

        all_rows.append(equipment_data)

    return pd.concat(all_rows, ignore_index=True)


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    output_path = project_root / "data" / "sample_sensor_data.csv"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    sensor_data = generate_sensor_data()
    sensor_data.to_csv(output_path, index=False)

    print(f"Generated sample sensor data: {output_path}")
    print(f"Rows created: {len(sensor_data)}")
    print(f"Anomalies created: {sensor_data['is_anomaly'].sum()}")


if __name__ == "__main__":
    main()