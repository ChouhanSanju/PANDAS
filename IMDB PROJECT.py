#1.
import pandas as pd
data=pd.read_csv(r'/content/IMDB-Movie-Data.csv')
print(data)

#2.
data.head(5)

#3.
print(data.info())

#4.
data.columns[data.isnull().any()]
data.columns

#5.
essential_columns=["Title","Rating","Runtime(Minutes)","Genre"]
print(data(essential_columns))

#6.
average_runtime=data["Runtime(Minutes)"].mean()
print("Average runtime of movies :-",average_runtime)

#7.
#presenting information visusally
import matplotlib.pyplot as plt
genre_counts = data["Genre"].str.split(",", expand=True).stack().value_counts()
genre_counts.plot(kind="bar", figsize=(10, 6), title="Number of Movies in Each Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.show()

#8.
director_counts = data["Director"].value_counts()
top_directors = director_counts.head(5)
print(top_directors)

#9.
# Convert the "Year" column to numeric and drop missing values
data["Year"] = pd.to_numeric(df["Year"], errors="coerce")
data = data.dropna(subset=["Year"])

year_counts = data["Year"].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(year_counts.index, year_counts.values, marker='o')
plt.title("Number of Movies Released Each Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.show()

#10.
plt.figure(figsize=(10, 6))
plt.hist(data["Runtime (Minutes)"], bins=20, edgecolor='k')
plt.title("Distribution of Movie Runtimes")
plt.xlabel("Runtime (Minutes)")
plt.ylabel("Frequency")
plt.show()

#11.
plt.figure(figsize=(10, 6))
plt.hist(data["Rating"], bins=20, edgecolor='k')
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

#12.
correlation = data["Rating"].corr(data["Runtime (Minutes)"])
print("Correlation between Ratings and Runtimes:", correlation)

#13.
top_actors = data["Actors"].str.split(', ').explode().value_counts().head(3)
print(top_actors)

#14.
plt.figure(figsize=(10, 6))
plt.scatter(data["Rating"], data["Revenue (Millions)"])
plt.title("Relationship between Movie Ratings and Box Office Earnings")
plt.xlabel("Rating")
plt.ylabel("Box Office Earnings (Millions)")
plt.show()

#15.
# Assuming there's a 'Language' column in dataset
languages_counts = data['Language'].value_counts()
print(languages_counts)
# Plotting the language counts
plt.figure(figsize=(10, 6))
languages_counts.plot(kind='bar')
plt.title('Distribution of Movies by Language')
plt.xlabel('Language')
plt.ylabel('Number of Movies')
plt.show()

#16.
plt.hist(data['Revenue (Millions)'], bins=20, edgecolor='k')
plt.xlabel('Revenue (Millions)')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movie Revenues')
plt.show()

#17.
production_company_counts = data['Director'].value_counts()
highest_director = production_company_counts.idxmax()
print(f"The director with the highest number of movies is: {highest_director}")

#18.
country_counts = data['Country'].value_counts()

# Plotting the country counts
plt.figure(figsize=(12, 8))
country_counts[:15].plot(kind='bar')
plt.title('Distribution of Movies by Country')
plt.xlabel('Country')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.show()

#19.
from wordcloud import WordCloud
titles = ' '.join(data['Title'])
# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
# Display the word cloud using matplotlib
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Word Cloud of Movie Titles')
plt.axis('off')
plt.show()

#20.
average_ratings_by_year = data.groupby('Year')['Rating'].mean()
average_ratings_by_year.plot(kind='line', marker='o', figsize=(10, 6))
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.title('Average Movie Ratings Over the Years')
plt.show()

#22.
director_actor_pairs = data.groupby(['Director', 'Actors']).size().sort_values(ascending=False)
most_common_pair = director_actor_pairs.head(1)
print(most_common_pair)

#23.
yearly_runtimes = data.groupby('Year')['Runtime (Minutes)'].mean()
plt.plot(yearly_runtimes.index, yearly_runtimes.values)
plt.xlabel('Year')
plt.ylabel('Average Runtime (Minutes)')
plt.title('Change in Movie Runtimes Over the Years')
plt.show()

#25.
from collections import Counter
keywords = Counter(" ".join(df['Description']).split()).most_common(10)
print("Top 10 Keywords from Movie Descriptions:")
print(keywords)


#26.
comparison_metrics = ['Rating', 'Revenue (Millions)']
data[comparison_metrics].plot(kind='bar', figsize=(10, 6))
plt.xlabel('Movies')
plt.ylabel('Values')
plt.title('Comparison of Rating and Revenue')
plt.show()

#27.
plt.boxplot(data['Runtime (Minutes)'])
plt.ylabel('Runtime (Minutes)')
plt.title('Boxplot of Movie Runtimes')
plt.show()

#29.
for genre in data['Genre'].str.split(',').explode().unique():
    genre_data = data[data['Genre'].str.contains(genre, na=False)]
    plt.hist(genre_data['Rating'], alpha=0.5, label=genre, bins=15)

plt.legend()
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.title('Distribution of Ratings for Different Genres')
plt.show()

#28.
plt.scatter(data['Votes'], data['Rating'])
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Relationship Between Votes and Movie Ratings')
plt.show()

#30.
plt.figure(figsize=(8, 6))
plt.boxplot(data['Runtime'])
plt.title('Box Plot of Movie Runtimes')
plt.ylabel('Runtime (minutes)')
plt.xticks([1], ['Movies'])
plt.show()



