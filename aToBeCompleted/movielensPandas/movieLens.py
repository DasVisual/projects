#! python3

import pandas as pd
import matplotlib.pyplot as plt


user_columns = ['user_id', 'age', 'gender']

users = pd.read_csv('C:/Users/noona/Downloads/python/projects/aToBeCompleted/movielensPandas/ml-100k/u.user', sep= '|', names=user_columns, usecols=range(3))

ratings_columns = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('C:/Users/noona/Downloads/python/projects/aToBeCompleted/movielensPandas/ml-100k/u.data', sep= '\t', names= ratings_columns, usecols=range(3))

movie_columns = ['movie_id', 'title']
movies = pd.read_csv('C:/Users/noona/Downloads/python/projects/aToBeCompleted/movielensPandas/ml-100k/u.item', sep= '|', names=movie_columns, usecols=range(2), encoding='iso-8859-1')

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
movie_data = pd.merge(movie_ratings, users)

# Top rated movies
print('Top rated movies (overall):\n', movie_data.groupby('title').size().sort_values(ascending = False)[:20])
print('\n')

# Find top rated movies for teens and oldies

oldies = movie_data[(movie_data.age > 60)]
# Get the top rated ones
oldies = oldies.groupby('title').size().sort_values(ascending=False)

# Extract movies for teens 
teens = movie_data[(movie_data.age > 12) & (movie_data.age < 20)]
# Get the top rated ones
teens = teens.groupby('title').size().sort_values(ascending=False)

print('Top ten movies for oldies: \n', oldies[:10])
print('\n')
print('Top ten movies for teens: \n', teens[:10])
print('\n')

ratings_by_title = movie_data.groupby('title').size()
popular_movies = ratings_by_title.index[ratings_by_title >= 250]

ratings_by_gender = movie_data.pivot_table('rating', index='title', columns='gender')
ratings_by_gender = ratings_by_gender.ix[popular_movies]
print('Rated movies by gender \n', ratings_by_gender.head())

top_movies_women = ratings_by_gender.sort_values(by= 'F', ascending=False)
print('Top rated movies by women \n', top_movies_women.head())

ratings_by_gender['diff'] = ratings_by_gender['M'] - ratings_by_gender['F']

print('Difference by gender \n', ratings_by_gender.head())

gender_diff = ratings_by_gender['diff']

# Only get absolute values
gender_diff = abs(gender_diff)
# Sort by size
gender_diff.sort_values(inplace=True, ascending=False)

# Show top 10 differences
gender_diff[:10].plot(kind='barh')
plt.show()




