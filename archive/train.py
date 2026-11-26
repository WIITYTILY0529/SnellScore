import pandas as pd

# Create example data
data = {
    'last_name, first_name': ['Smith, John', 'Smith, John', 'Smith, John',
                              'Doe, Jane', 'Doe, Jane', 'Doe, Jane',
                              'Lee, Chris', 'Lee, Chris', 'Lee, Chris'],
    'year': [2021, 2022, 2023, 2021, 2022, 2023, 2021, 2022, 2023],
    'snell_score': [55, 60, 58, 50, 52, 54, 62, 64, 63]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Extract each player's Snell Score for year n and year n+1
def get_year_n_and_n_plus_1(group):
    group_sorted = group.sort_values('year')  # Sort by year
    group_sorted['next_year_snell'] = group_sorted['snell_score'].shift(-1)  # Snell Score for year n+1
    return group_sorted.dropna(subset=['next_year_snell'])  # Drop NaN values

# Extract year-n and year-n+1 Snell Scores per player
df_filtered = df.groupby('last_name, first_name').apply(get_year_n_and_n_plus_1)
dff = df.groupby('last_name, first_name')
group_sorted = df.sort_values('year')
group_sorted['next_year_snell'] = group_sorted['snell_score'].shift(-1)

# X axis: year-n Snell Score, Y axis: year-n+1 Snell Score
x = df_filtered['snell_score']
y = df_filtered['next_year_snell']

# Calculate the correlation between Snell Scores
corr_value = x.corr(y)

print(df_filtered)
#print(df.sort_values('year'))
#print(group_sorted)  # Check Snell Scores by year

#print(f"Snell Score correlation across the full population: {corr_value}")
