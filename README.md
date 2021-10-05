# Movie-Recommendation-System

API Link : [https://moviefindapi.herokuapp.com/movie?title=insert-movie-name](https://moviefindapi.herokuapp.com/movie?title=insert-movie-name)

A movie recommendation API that uses a item-based collaborative filtering algorithm. It takes a movie input from the user and recommends 10 movies based on the entered movie. 
The TMDB 5000 movies dataset is used. It is built using python and deployed on Heroku.


File Description:

# get_data():-
get_data() is used to fetch the data about the movies and return the dataset with it's attributes as the result for further preprocessing.
# combine_data():-
combine_data() drops the columns not required for feature extraction and then combines the cast and genres column,finally returning the combine column as the result of this function.
# transform_data():-
transform_data() takes the value returned by combine_data() and the plot column from get_data() and applies CountVectorizer and TfidfVectorizer respectively and calculates the Cosine values.
# recommend_movies():-
recommend_movies() takes four parameters i.e movie_name and return values of get_data(), combine_data(), transform_data as input and returns the top 10 movies similar to our input movie.
# results():-
result() takes a movie's title as input and returns the top 10 recommendations using the recommend_movies() function.
# app.py
The Flask app where we use the recommend.py as a module and return the results in JSON format.
# requirements.txt
This has all the dependencies required to deploy our application on Heroku
# Procfile
A Procfile is a file which describes how to run your application.
