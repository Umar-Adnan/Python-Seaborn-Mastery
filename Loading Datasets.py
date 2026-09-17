import seaborn as sns

# print(sns.get_dataset_names())
tips_data = sns.load_dataset("tips")
print(tips_data.head())
print(tips_data.tail())