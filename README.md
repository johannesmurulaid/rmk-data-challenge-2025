# RMK Data Team Internship 2025 - Challenge Solution

This repository contains a solution to the RMK Data Team Internship test challenge for 2025.
The task is to simulate and visualize the probability that Rita arrives late to her 09:05 meeting based on different home departure times.

## Problem Summary
Rita takes Tallinn bus #8 every weekday from Zoo to Toompark to attend a 9:05 AM meeting. We model her commute:
- 5 minutes walk from home to Zoo stop
- 15 minutes average bus ride with potential delays
- 4 minutes walk from Toompark to office

Goal: For different departure times from home (08:00–08:50), calculate and plot her probability of arriving late.

## Project Structure
```
rmk-data-challenge-2025/
├── src/
│   └── simulate.py
├── tests/
│   └── test_simulate.py
├── requirements.txt
└── README.md
```

## Example Output
A line plot showing the probability of being late vs. the time Rita leaves home.

## How to Run

1. Clone the repository:
```
git clone https://github.com/YOUR_USERNAME/rmk-data-challenge-2025.git
cd rmk-data-challenge-2025
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the simulation:
```
python src/simulate.py
```

## Dependencies
```
pandas
numpy
matplotlib
seaborn
```

## Future Improvements
- Use real-time or historical GTFS data
- Add weather effect modeling
- Create a Streamlit app
- Add unit tests and parameter configuration
