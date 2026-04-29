# Edge-Based Real-Time Anomaly Detection System

## 📌 Overview

This project demonstrates a **real-time anomaly detection system** implemented at the **edge** using a lightweight machine learning approach.
Sensor data is generated continuously and processed locally to detect abnormal patterns instantly.


## 🎯 Aim

To design and implement an edge-based system that detects anomalies in real-time sensor data using a lightweight model, reducing latency and bandwidth usage.


## ⚙️ Features

* Real-time sensor data simulation
* Lightweight anomaly detection algorithm
* Instant alert generation
* Edge computing (local processing, no cloud dependency)
* Simple and easy-to-run implementation


## 🏗️ Project Structure

```
edge-anomaly-project/
│── realtime_main.py        # Main execution file
│── model.py                # Anomaly detection logic
│── sensor_simulator.py     # Real-time data generator
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
```


## 🔄 Working Principle

1. Sensor data is generated continuously
2. Data is processed locally on the edge device
3. A lightweight model checks for anomalies
4. If abnormal data is detected → alert is triggered


## 🧠 Algorithm

* Compute expected normal range (mean-based)
* Compare incoming value:

  ```
  |value - mean| > threshold → Anomaly
  ```
* Otherwise → Normal

---

## ▶️ How to Run

### Step 1: Install Dependencies

```
pip install -r requirements.txt
```

### Step 2: Run the Program

```
python realtime_main.py
```


## 📊 Sample Output

```
Starting Real-Time Edge Anomaly Detection...

Sensor Value: 25 -> Normal
Sensor Value: 27 -> Normal
Sensor Value: 85 -> Anomaly
ALERT: Anomaly Detected!
```


## 🚀 Applications

* Industrial fault detection
* Smart healthcare monitoring
* IoT-based systems
* Smart agriculture
* Network anomaly detection


## ✅ Advantages

* Low latency (real-time detection)
* Reduced bandwidth usage
* Works without internet
* Improved privacy


## ❌ Limitations

* Limited computational resources
* Uses simple model (less accurate than complex ML models)
* Fixed threshold may not adapt dynamically


## 🔮 Future Enhancements

* Add live data visualization (graphs)
* Integrate cloud alerts (Edge + Cloud system)
* Use advanced ML models (Isolation Forest, Autoencoders)
* Deploy on real IoT hardware (Raspberry Pi)


## 🧠 Key Concept

This project demonstrates how **edge computing** enables faster and efficient data processing by performing computations locally instead of relying on cloud servers.

