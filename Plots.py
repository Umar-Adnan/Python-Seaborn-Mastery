import seaborn as sns
import matplotlib.pyplot as plt
tips_data = sns.load_dataset("tips")
sns.scatterplot(tips_data, x = 'Total bill', y = 'Tip')
plt.show()