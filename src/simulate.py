import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns

WALK_HOME_TO_STOP = 300
WALK_STOP_TO_OFFICE = 240
BUS_TRAVEL_TIME = 900
BUS_FREQ = 600
BUS_STDDEV = 120
MEETING_TIME = datetime.strptime("09:05", "%H:%M")

def simulate_arrival_probability(leave_time_str: str, num_simulations: int = 1000) -> float:
    leave_time = datetime.strptime(leave_time_str, "%H:%M")
    late_count = 0
    for _ in range(num_simulations):
        walk_start = leave_time + timedelta(seconds=WALK_HOME_TO_STOP)
        minutes_past_hour = (walk_start.minute * 60 + walk_start.second)
        bus_wait_time = BUS_FREQ - (minutes_past_hour % BUS_FREQ)
        scheduled_bus_departure = walk_start + timedelta(seconds=bus_wait_time)
        delay = np.random.normal(loc=0, scale=BUS_STDDEV)
        actual_bus_departure = scheduled_bus_departure + timedelta(seconds=delay)
        arrival_at_destination = actual_bus_departure + timedelta(seconds=BUS_TRAVEL_TIME)
        final_arrival = arrival_at_destination + timedelta(seconds=WALK_STOP_TO_OFFICE)
        if final_arrival.time() > MEETING_TIME.time():
            late_count += 1
    return late_count / num_simulations

def plot_probabilities(start="08:00", end="08:50", step_minutes=1):
    times = []
    probs = []
    current = datetime.strptime(start, "%H:%M")
    end_time = datetime.strptime(end, "%H:%M")
    while current <= end_time:
        time_str = current.strftime("%H:%M")
        prob = simulate_arrival_probability(time_str)
        times.append(time_str)
        probs.append(prob)
        current += timedelta(minutes=step_minutes)
    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 6))
    plt.plot(times, probs, marker="o")
    plt.xticks(rotation=45)
    plt.title("Probability of Rita Being Late vs. Home Departure Time")
    plt.xlabel("Leave Home Time")
    plt.ylabel("Probability of Being Late")
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_probabilities()

