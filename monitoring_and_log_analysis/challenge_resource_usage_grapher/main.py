import matplotlib.pyplot as plt

def plot_memory_usage(memory_usage):
    # Write your code here
    time_points = list(range(len(memory_usage)))
    plt.plot(time_points, memory_usage, color = "Green", marker = "x", linestyle = "--")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Memory Usage (MB)")
    plt.title("Memory Usage Over Time")
    pass

sample_memory_usage = [512, 530, 545, 600, 620, 610, 590, 650, 670, 680]
plot_memory_usage(sample_memory_usage)
