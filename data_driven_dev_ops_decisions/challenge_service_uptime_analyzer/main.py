import pandas as pd

def analyze_uptime(data, threshold):
    # Write your code here
    df = pd.DataFrame(data)
    avg_uptime = df["uptime_hours"].mean()
    print(f"Average uptime across servers: {avg_uptime:.2f} hours")
    # Example placeholder for underperforming servers
    underperforming = df[df["uptime_hours"] < threshold]
    if not underperforming.empty:
        print("Servers below threshold:")
        print(underperforming[['server', 'uptime_hours']])
    else:
        print("All servers meet or exceed the uptime threshold.")

service_data = [
    {'server': 'A', 'uptime_hours': 98},
    {'server': 'B', 'uptime_hours': 120},
    {'server': 'C', 'uptime_hours': 85},
    {'server': 'D', 'uptime_hours': 110},
    {'server': 'E', 'uptime_hours': 77}
]
threshold = 90
analyze_uptime(service_data, threshold)
