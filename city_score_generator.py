import pandas as pd
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('city.csv')

# Self Defined Weight
weights = {
    'Attractions and Culture': 0.4,
    'Cuisine': 0.3,
    'Accessibility': 0.2,
    'Infrastructure and Safety': 0.1
}

attractions_culture_feature = 'Attraction number'
cuisine_features = ['Rural food expenditure', 'Urban food expenditure']
accessibility_features = ['AR_capita', 'OD_capita']
infrastructure_safety_features = ['  % local hukou rate', 'Resident population density', '% under age 14', '% between ages 15 and 64', '% above age 65']
#print(df.columns)

scaler = MinMaxScaler()
df[attractions_culture_feature] = scaler.fit_transform(df[attractions_culture_feature].values.reshape(-1, 1))
df[cuisine_features] = scaler.fit_transform(df[cuisine_features])
df[accessibility_features] = scaler.fit_transform(df[accessibility_features])
df[infrastructure_safety_features] = scaler.fit_transform(df[infrastructure_safety_features])

df['Attractions and Culture'] = 10* df[attractions_culture_feature]
df['Cuisine'] = 10* df[cuisine_features].mean(axis=1)
df['Accessibility'] = 10* df[accessibility_features].mean(axis=1)
df['Infrastructure and Safety'] = 10* df[infrastructure_safety_features].mean(axis=1)


cities = ['Beijing', 'Shanghai', "Xi'an City", 'Guilin City', 'Chengdu City', 'Hangzhou City', 'Suzhou City', 'Shenzhen City', 'Guangzhou', 'Lhasa City', 'Lijiang City', 'Dali Bai A.P', 'Chongqing', 'Nanjing City', 'Harbin City']

result = df[['Region', 'Attractions and Culture', 'Cuisine', 'Accessibility', 'Infrastructure and Safety']]
filtered_result = result[result['Region'].isin(cities)]

filtered_result.to_csv('city_score.csv', index=False)
