class AnomalyDetector:
    def __init__(self, threshold=15):
        self.threshold = threshold
        self.mean = 25

    def predict(self, value):
        if abs(value - self.mean) > self.threshold:
            return "Anomaly"
        return "Normal"
