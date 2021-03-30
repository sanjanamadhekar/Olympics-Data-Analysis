# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading
data = pd.read_csv(path)

data.rename(columns={'Total': 'Total_Medals'}, inplace=True)

data.head(10)

# Summer or Winter

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', data['Better_Event'])

better_event = data['Better_Event'].value_counts().idxmax()

# Top 10

top_countries = data[['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']]

top_countries.drop('Total_Medals', axis=1)

top_countries = top_countries[:-1]


def top_ten(top_countries, col):
    country_list = list(top_countries.nlargest(10, col)['Country_Name'])
    return country_list


top_10_summer = top_ten(top_countries, 'Total_Summer')

top_10_winter = top_ten(top_countries, 'Total_Winter')

top_10 = top_ten(top_countries, 'Total_Medals')

common = list(set(top_10_summer).intersection(top_10_winter).intersection(top_10))

# Plotting top 10

fig, ax = plt.subplots(3)

summer_df = data[data['Country_Name'].isin(top_10_summer)]

ax[0].bar(summer_df['Country_Name'], summer_df['Total_Summer'])

winter_df = data[data['Country_Name'].isin(top_10_winter)]

ax[1].bar(winter_df['Country_Name'], winter_df['Total_Winter'])

top_df = data[data['Country_Name'].isin(top_10)]

ax[2].bar(top_df['Country_Name'], top_df['Total_Winter'])

ax[0].set(xlabel='Country_Name', ylabel='Total_Summer')
ax[1].set(xlabel='Country_Name', ylabel='Total_Winter')
ax[2].set(xlabel='Country_Name', ylabel='Total_Medals')

# Top Performing Countries

summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']

summer_max_ratio = summer_df['Golden_Ratio'].max()

summer_country_gold = summer_df['Golden_Ratio'].idxmax()

summer_country_gold = summer_df['Country_Name'][summer_country_gold]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']

winter_max_ratio = winter_df['Golden_Ratio'].max()

winter_country_gold = winter_df['Golden_Ratio'].idxmax()

winter_country_gold = winter_df['Country_Name'][winter_country_gold]

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']

top_max_ratio = top_df['Golden_Ratio'].max()

top_country_gold = top_df['Golden_Ratio'].idxmax()

top_country_gold = top_df['Country_Name'][top_country_gold]

# Best in the world

data_1 = data[:-1]

data_1['Total_Points'] = data_1['Gold_Total'] * 3 + data_1['Silver_Total'] * 2 + data_1['Bronze_Total']

most_points = data_1['Total_Points'].max()

best_country = data_1['Country_Name'][data_1['Total_Points'].idxmax()]

# Plotting the best

best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]

best.plot.bar(stacked=True)
locs, labels = plt.xticks()
new_xticks = [best_country for d in locs]
plt.xticks(locs, new_xticks, rotation=45, horizontalalignment='right')

plt.xlabel('United States')

plt.ylabel('Medals Tally')


