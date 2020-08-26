# Predict IMDB movie rating

The goal of this project is to tell how good call we tell that a movie will have a great IMDB score by measuring the variables that impacts it

## First Part - Parsing data

To do so, we used the IMDB API to get data about a number of movies like the casting information, directors, production companies, awards, genres, budget, gross, description, imdb_rating, etc.

## Second Part - Data Analysis

The second part consist of analysing the dataframe and measuring the correlation between the variables. For example, are the movie awards correlated to the worlwide gross? Does the more a movie is liked, the more the casting is liked ?

See the jupyter notebook to get the results of the exploration.

is to analyze the dataframe and observe correlation between variables. For example, are the movie awards correlated to the worlwide gross ? Does the more a movie is a liked, the more the casting is liked ? 
See the jupyter notebook file.  

As we can see in the pictures above, the imdb score is correlated to the number of awards and the gross but not really to the production budget and the number of facebook likes of the casting.  
Obviously, domestic and worlwide gross are highly correlated. However, the more important the production budget, the more important the gross.  
As it is shown in the notebook, the budget is not really correlated to the number of awards.  
What's funny is that the popularity of the third most famous actor is more important for the IMDB score than the popularity of the most famous score (Correlation 0.2 vs 0.08).  
(Many other charts in the Jupyter notebook)

## Third Part - Predict the IMDB score

The goal of this part is to predict the IMDB score.#   e d a - i m d b s c o r e  
 #   e d a - i m d b s c o r e  
 