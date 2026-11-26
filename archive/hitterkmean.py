from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_csv('data/raw/bb%.csv')

# Select the feature columns
features = df[['bb_percent', 'oz_swing_percent', 'z_swing_percent']]

# K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Split into 3 clusters
df['cluster'] = kmeans.fit_predict(features)

# Select a specific cluster (e.g. the one that matches the criteria)
filtered_df = df[df['cluster'] == 2]  # Cluster numbers depend on the data
print(filtered_df)


df['bb_percent_percentile'] = df.apply(calculate_percentiles, axis=1, column='bb_percent', data=df)
df['bb_percent_percentile'] = df['bb_percent_percentile'].apply(
    lambda value : top_25(value)
    )
df['meatball_percent_percentile'] = df.apply(calculate_percentiles, axis=1, column='meatball_percent', data=df)
df['meatball_percent_percentile'] = 1 - df['meatball_percent_percentile']
df['meatball_percent_percentile'] = df['meatball_percent_percentile'].apply(
    lambda value : top_25(value)
    )

'''top_players[['bb_percent_normalized', 'oz_swing_percent_normalized', 'z_swing_percent_normalized']].plot(kind='bar', stacked=True)
plt.title('Top 10 Players by Normalized Score')
plt.ylabel('Normalized Percentile')
plt.xlabel('Player Index')
plt.show()'''