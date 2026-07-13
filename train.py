import pandas as pd

# 예제 데이터 생성
data = {
    'last_name, first_name': ['Smith, John', 'Smith, John', 'Smith, John',
                              'Doe, Jane', 'Doe, Jane', 'Doe, Jane',
                              'Lee, Chris', 'Lee, Chris', 'Lee, Chris'],
    'year': [2021, 2022, 2023, 2021, 2022, 2023, 2021, 2022, 2023],
    'snell_score': [55, 60, 58, 50, 52, 54, 62, 64, 63]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 선수별로 n년도와 n+1년도 Snell Score 추출
def get_year_n_and_n_plus_1(group):
    group_sorted = group.sort_values('year')  # 연도 순 정렬
    group_sorted['next_year_snell'] = group_sorted['snell_score'].shift(-1)  # n+1년 Snell Score
    return group_sorted.dropna(subset=['next_year_snell'])  # NaN 값 제거

# 선수별 n년도와 n+1년도의 Snell Score 추출
df_filtered = df.groupby('last_name, first_name').apply(get_year_n_and_n_plus_1)
dff = df.groupby('last_name, first_name')
group_sorted = df.sort_values('year')
group_sorted['next_year_snell'] = group_sorted['snell_score'].shift(-1)

# X축: n년도 Snell Score, Y축: n+1년도 Snell Score
x = df_filtered['snell_score']
y = df_filtered['next_year_snell']

# Snell Score 간 상관계수 계산
corr_value = x.corr(y)

print(df_filtered)
#print(df.sort_values('year'))
#print(group_sorted)  # 연도별 Snell Score 확인

#print(f"전체 모집단의 Snell Score 상관계수: {corr_value}")
