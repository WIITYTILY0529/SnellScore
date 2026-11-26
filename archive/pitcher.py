import pandas as pd
from scipy.stats import percentileofscore
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/raw/pitcher.csv')

def standardized(series):
    return (series - series.mean())/series.std(ddof=0)

def scale_20_80(z_scores):
    return 50 + (z_scores*10)

df['bb_percent_z'] = standardized(df['bb_percent'])
df['bb_percent_scale'] = scale_20_80(df['bb_percent_z'])
df['meatball_z'] = -standardized(df['meatball_percent'])
df['meatball_scale'] = scale_20_80(df['meatball_z'])
df['snell_score'] = df['bb_percent_scale'] + df['meatball_scale']
df_filtered = df[(df['bb_percent_scale'] >= 60) & (df['meatball_scale'] >=60)]
df_filtered = df_filtered.dropna(axis = 0)

df_filtered = df_filtered[['last_name, first_name', 'year', 'bb_percent', 'bb_percent_scale', 'meatball_percent', 'meatball_scale', 'snell_score']]
sorted_df = df_filtered.sort_values(by = 'snell_score', ascending= False)


# Extract each player's Snell Score for year n and year n+1
def get_year_n_and_n_plus_1(group):
    # Get the year-n and year-n+1 Snell Score for each player
    group_sorted = group.sort_values('year')  # Sort by year
    group_sorted['next_year_snell'] = group_sorted['snell_score'].shift(-1)  # Snell Score for year n+1
    return group_sorted.dropna(subset=['next_year_snell'])  # Drop rows without a year n+1

# Extract year-n and year-n+1 Snell Scores per player across the full dataset
df_filtered = df.groupby('last_name, first_name').apply(get_year_n_and_n_plus_1)

# X axis: year-n Snell Score, Y axis: year-n+1 Snell Score
x = df_filtered['snell_score']
y = df_filtered['next_year_snell']

# Calculate the correlation between Snell Scores
corr_value = x.corr(y)

print(f"Snell Score correlation across the full population: {corr_value}")

sorted_df.to_csv('snellscorepitcher.csv')
