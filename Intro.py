import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load and Clean Dataset
df = pd.read_csv("global_terrorism_2000_2017_subset.csv")
df["nkill"] = df["nkill"].fillna(0)

# Filter for Asian regions
asian_regions = [
    'South Asia', 'Southeast Asia', 'East Asia',
    'Central Asia', 'Middle East & North Africa'
]
asia_df = df[df['region_txt'].isin(asian_regions)].copy()

# 2. Aggregate Data using Pandas
summary_df = asia_df.groupby('country_txt').agg(
    Total_Attacks=('iyear', 'count'),
    Total_Fatalities=('nkill', 'sum')
).reset_index()

top10_df = summary_df.sort_values(by='Total_Attacks', ascending=False).head(10)

# 3. Create Scatter Plot with Seaborn
plt.figure(figsize=(9, 6))
sns.set_theme(style="whitegrid")

sns.scatterplot(
    data=top10_df,
    x='Total_Attacks',
    y='Total_Fatalities',
    hue='country_txt',  # Color points by country automatically
    s=150               # Set point size
)

plt.title('Total Attacks vs. Fatalities across Top 10 Asian Nations', fontweight='bold')
plt.xlabel('Total Incident Count')
plt.ylabel('Total Fatalities')

plt.tight_layout()
plt.savefig("seaborn_scatterplot.png", dpi=300, bbox_inches="tight")
plt.show()