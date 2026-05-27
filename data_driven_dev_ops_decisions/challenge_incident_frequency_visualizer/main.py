import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_incident_frequencies():
    data = {
        "incident_type": [
            "network", "application", "hardware", "network", "application",
            "network", "hardware", "application", "network", "hardware",
            "application", "application", "hardware", "network", "hardware"
        ]
    }
    df = pd.DataFrame(data)
    # Write your code here
    incident_counts = df["incident_type"].value_counts().reset_index()
    incident_counts.columns = ["incident_type", "count"]
    ax = sns.barplot(data=incident_counts, x="incident_type", y="count")
    sns.set_palette("pastel")
    ax.set_title("Incident Frequency by Type")
    ax.set_xlabel("Incident Type")
    ax.set_ylabel("Frequency")
    plt.show()
        
    
    
visualize_incident_frequencies()