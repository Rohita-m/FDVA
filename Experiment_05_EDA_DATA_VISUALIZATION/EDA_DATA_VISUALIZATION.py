import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load Data
df = pd.read_csv("data.csv") # Replace with your file
print("Data Head:")
print(df.head())

print("\n--- LINE CHART ---")
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, color='blue', label='Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.legend()
plt.savefig('Line_Chart.png')
plt.show()

print("\n--- BAR CHART ---")
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 4]

plt.bar(categories, values, color='orange')
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.savefig('Bar_Chart.png')
plt.show()

print("\n--- HISTOGRAM ---")
data = np.random.randn(1000)

plt.hist(data, bins=20, color='purple', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.savefig('Histogram.png')
plt.show()

print("\nAll visualizations generated successfully.")
