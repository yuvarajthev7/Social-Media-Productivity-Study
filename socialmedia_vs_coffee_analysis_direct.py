import pandas as pd

df=pd.read_csv('social_media_vs_productivity.csv')
print("First 5 rows of the dataset")
df.head(5)
print("\ndataframe info")
df.info()
print("\nmissing values before cleaning")
df.isnull().sum()
# columns identified with missing values and we impute them
numerical_cols_to_impute = [
    'daily_social_media_time',
    'perceived_productivity_score',
    'actual_productivity_score',
    'stress_level',
    'sleep_hours',
    'screen_time_before_sleep',
    'job_satisfaction_score'
]

print("Imputation with Median")
for col in numerical_cols_to_impute:
    if df[col].isnull().any():
        median_val = df[col].median()
        df.loc[:, col] = df[col].fillna(median_val)
        print(f"Filled NaN in '{col}' with median: {median_val:.2f}")

# verification
print("\nMissing Values Count After Cleaning")
df.isnull().sum() # updated NaN checker
print("average daily coffee consumption by social media platform preference")
avg_coffee_by_platform = df.groupby('social_platform_preference')['coffee_consumption_per_day'].mean().sort_values(ascending=False)
print(avg_coffee_by_platform)
print("\nmedian daily coffee consumption by social platform preference")
median_coffee_by_platform = df.groupby('social_platform_preference')['coffee_consumption_per_day'].median().sort_values(ascending=False)
print(median_coffee_by_platform)
print("\nnumber of users per social platform preference")
platform_counts = df['social_platform_preference'].value_counts()
print(platform_counts)
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 7))
sns.barplot(x=avg_coffee_by_platform.index, y=avg_coffee_by_platform.values, palette='crest')
plt.title('Average Daily Coffee Consumption by Social Media Platform Preference', fontsize=16)
plt.xlabel('Social Media Platform Preference', fontsize=12)
plt.ylabel('Average Coffee Consumption (cups/day)', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
plt.figure(figsize=(12, 7))
sns.boxplot(x='social_platform_preference', y='coffee_consumption_per_day', data=df, palette='crest')
plt.title('Daily Coffee Consumption Distribution by Social Media Platform Preference', fontsize=16)
plt.xlabel('Social Media Platform Preference', fontsize=12)
plt.ylabel('Coffee Consumption (cups/day)', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
