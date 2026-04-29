import random
import time

def generate_sensor_data():
    while True:
        value = random.randint(20, 30)
        if random.random() < 0.1:
            value = random.randint(70, 100)
        yield value
        time.sleep(1)
