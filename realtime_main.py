from model import AnomalyDetector
from sensor_simulator import generate_sensor_data

model = AnomalyDetector(threshold=15)

print("Starting Real-Time Edge Anomaly Detection...\n")

sensor_stream = generate_sensor_data()

for value in sensor_stream:
    result = model.predict(value)
    print(f"Sensor Value: {value} -> {result}")

    if result == "Anomaly":
        print("ALERT: Anomaly Detected!\n")
