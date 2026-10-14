from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_csv('C:/Users/choim/choiminseok/Baseball/01_Research/09_SnellScore/data/raw/bb%.csv')

# 사용할 열 선택
features = df[['bb_percent', 'oz_swing_percent', 'z_swing_percent']]

# K-means 클러스터링
kmeans = KMeans(n_clusters=3, random_state=42)  # 3개의 클러스터로 나누기
df['cluster'] = kmeans.fit_predict(features)

# 특정 클러스터 선택 (예: 조건에 맞는 클러스터 찾기)
filtered_df = df[df['cluster'] == 2]  # 클러스터 번호는 데이터에 따라 다름
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