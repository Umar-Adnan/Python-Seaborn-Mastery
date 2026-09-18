import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load and clean dataset
df = pd.read_csv("global_terrorism_2000_2017_subset.csv")
df["nkill"] = df["nkill"].fillna(0)

asian_regions = [
    'South Asia', 'Southeast Asia', 'East Asia', 
    'Central Asia', 'Middle East & North Africa'
]
asia_df = df[df['region_txt'].isin(asian_regions)].copy()

# 2. Configure Seaborn Dark Theme
sns.set_theme(style="dark", rc={
    "axes.facecolor": "#121212",      # Plot background
    "figure.facecolor": "#121212",    # Canvas background
    "grid.color": "#2a2a2a",          # Subtle dark grid lines
    "text.color": "white",            # Default text color
    "axes.labelcolor": "white",      # Axis label color
    "xtick.color": "white",           # X-axis tick marks
    "ytick.color": "white",           # Y-axis tick marks
    "legend.labelcolor": "white"      # Legend text color
})

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Asian Security & Conflict Analytics: Dark Mode Dashboard", fontsize=18, fontweight='bold', color="white", y=0.98)

# --- Plot 1: Heatmap (Magma Colormap for Dark Backgrounds) ---
top8_countries = asia_df['country_txt'].value_counts().head(8).index
top8_df = asia_df[asia_df['country_txt'].isin(top8_countries)]
ct = pd.crosstab(top8_df['attacktype1_txt'], top8_df['country_txt'])

heatmap = sns.heatmap(ct, cmap="magma", annot=True, fmt="d", cbar=True, ax=axes[0, 0], linewidths=0.5, linecolor="#121212")
axes[0, 0].set_title("1. Attack Tactics Distribution (Heatmap)", fontweight='bold', fontsize=13, color="white")
axes[0, 0].set_xlabel("Country", fontweight='bold', color="white")
axes[0, 0].set_ylabel("Attack Type", fontweight='bold', color="white")
axes[0, 0].tick_params(axis='x', rotation=45, colors="white")
axes[0, 0].tick_params(axis='y', colors="white")

# Adjust colorbar label color for dark canvas
cbar = heatmap.collections[0].colorbar
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(plt.getp(cbar.ax, 'yticklabels'), color='white')

# --- Plot 2: Boxplot (Log Scale) ---
top_attacks = asia_df['attacktype1_txt'].value_counts().head(5).index
attack_df = asia_df[asia_df['attacktype1_txt'].isin(top_attacks)].copy()
attack_fatalities = attack_df[attack_df['nkill'] > 0]

sns.boxplot(data=attack_fatalities, x='nkill', y='attacktype1_txt', palette="Set2", ax=axes[0, 1])
axes[0, 1].set_xscale('log')
axes[0, 1].set_title("2. Fatalities Distribution per Incident (Boxplot)", fontweight='bold', fontsize=13, color="white")
axes[0, 1].set_xlabel("Fatalities per Incident (Log Scale)", fontweight='bold', color="white")
axes[0, 1].set_ylabel("Attack Type", fontweight='bold', color="white")

# --- Plot 3: Lineplot (High Contrast Palette) ---
top4_asia = asia_df[asia_df['country_txt'].isin(['Iraq', 'Afghanistan', 'Pakistan', 'India'])]

sns.lineplot(data=top4_asia, x='iyear', y='nkill', hue='country_txt', marker='o', linewidth=2.5, palette="bright", ax=axes[1, 0])
axes[1, 0].set_title("3. Yearly Mean Fatalities per Incident (Lineplot)", fontweight='bold', fontsize=13, color="white")
axes[1, 0].set_xlabel("Year", fontweight='bold', color="white")
axes[1, 0].set_ylabel("Mean Fatalities", fontweight='bold', color="white")
legend3 = axes[1, 0].legend(title="Country", facecolor="#1e1e1e", edgecolor="#333333")
plt.setp(legend3.get_texts(), color='white')
plt.setp(legend3.get_title(), color='white')

# --- Plot 4: Barplot (Neon Accent Colors) ---
top_targets = asia_df['targtype1_txt'].value_counts().head(6).index
target_df = asia_df[asia_df['targtype1_txt'].isin(top_targets)]

sns.barplot(data=target_df, x='targtype1_txt', y='nkill', hue='success', palette={1: "#ff4d4d", 0: "#00b3b3"}, estimator=sum, errorbar=None, ax=axes[1, 1])
axes[1, 1].set_title("4. Total Fatalities by Target & Success Status", fontweight='bold', fontsize=13, color="white")
axes[1, 1].set_xlabel("Target Type", fontweight='bold', color="white")
axes[1, 1].set_ylabel("Total Cumulative Fatalities", fontweight='bold', color="white")
axes[1, 1].tick_params(axis='x', rotation=35, colors="white")
legend4 = axes[1, 1].legend(title="Attack Success", labels=["Failed (0)", "Successful (1)"], facecolor="#1e1e1e", edgecolor="#333333")
plt.setp(legend4.get_texts(), color='white')
plt.setp(legend4.get_title(), color='white')

# --- Export with Dark Facecolor Preserved ---
plt.tight_layout()
plt.savefig("seaborn_dark_dashboard.png", dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.show()