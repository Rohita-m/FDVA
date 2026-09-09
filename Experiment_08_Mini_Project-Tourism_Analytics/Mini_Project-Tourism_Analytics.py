import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cost Components by Country (Grouped Bar Chart)
cost_df = pd.read_csv("cost_data.csv")
cost_df = cost_df.set_index('Country')

fig, axes = plt.subplots(3, 2, figsize=(15, 18))
plt.subplots_adjust(hspace=0.4)

cost_df.plot(kind='bar', ax=axes[0, 0], colormap='Set3')
axes[0, 0].set_title('Cost Components by Country')
axes[0, 0].set_ylabel('Index Value')
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. Festival Frequency by Month
fest_freq = pd.read_csv("festival_freq.csv")
axes[0, 1].plot(fest_freq['Month'], fest_freq['Number of Festivals'], marker='s', color='crimson')
axes[0, 1].set_title('Festival Frequency by Month')
axes[0, 1].set_xlabel('Month')
axes[0, 1].set_ylabel('Number of Festivals')
axes[0, 1].set_xticks(range(1, 13))

# 3. Festival Impact Score Distribution by Season
fest_impact = pd.read_csv("festival_impact.csv")
sns.boxplot(x='Season', y='Festival Impact Score', data=fest_impact, notch=True, ax=axes[1, 0], palette='Pastel1')
axes[1, 0].set_title('Festival Impact Score Distribution by Season')

# 4. Seasonal Tourist Movement Transitions
tourism_df = pd.read_csv("tourism_data.csv")
pivot = tourism_df.pivot_table(index='Origin Season', columns='Destination Season', values='Movement Flow', aggfunc='mean')
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="Purples", ax=axes[1, 1])
axes[1, 1].set_title('Seasonal Tourist Movement Transitions')

# 5. Seasonal Festival Distribution
season_counts = fest_impact['Season'].value_counts()
season_counts.plot(kind='bar', ax=axes[2, 0], color=['lightcoral', 'navajowhite', 'lightsteelblue', 'cornflowerblue'], edgecolor='black')
axes[2, 0].set_title('Seasonal Festival Distribution')
axes[2, 0].set_ylabel('Number of Festivals')
axes[2, 0].tick_params(axis='x', rotation=0)
for i, v in enumerate(season_counts):
    axes[2, 0].text(i, v + 2, str(v), ha='center', fontweight='bold')

axes[2, 1].axis('off') # Hide unused subplot

plt.tight_layout()
plt.savefig('Tourism_Analytics_Dashboard.png')
print("Visualizations successfully saved to Tourism_Analytics_Dashboard.png")
