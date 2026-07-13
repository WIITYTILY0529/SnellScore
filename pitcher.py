import pandas as pd
from scipy.stats import percentileofscore
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/choiminseok/Desktop/최민석/야구/볼넷의 역설/pitcher.csv')

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


# 선수별로 n년도와 n+1년도 Snell Score 추출
def get_year_n_and_n_plus_1(group):
    # 각 선수에 대해 n년도와 n+1년도 Snell Score를 가져옴
    group_sorted = group.sort_values('year')  # 연도 순으로 정렬
    group_sorted['next_year_snell'] = group_sorted['snell_score'].shift(-1)  # n+1년도의 Snell Score
    return group_sorted.dropna(subset=['next_year_snell'])  # n+1년도가 없는 경우 제외

# 전체 데이터에서 선수별로 n년도와 n+1년도의 Snell Score 추출
df_filtered = df.groupby('last_name, first_name').apply(get_year_n_and_n_plus_1)

# X축: n년도 Snell Score, Y축: n+1년도 Snell Score
x = df_filtered['snell_score']
y = df_filtered['next_year_snell']

# Snell Score 간 상관계수 계산
corr_value = x.corr(y)

print(f"전체 모집단의 Snell Score 상관계수: {corr_value}")

sorted_df.to_csv('snellscorepitcher.csv')
