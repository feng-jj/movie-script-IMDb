# movie-script-IMDb
In the present day, the entertainment industry is constantly evolving toward making the most enjoyable and profitable sources of film entertainment. Through the use of movie rating sites, we can now decide whether or not it is worth the trip to the movie theatre to watch a partiuclar film.

With this in mind, I was interested in seeing how we could predict whether or not a movie is worth watching just by analyzing its script.
Is there a correlation between certain word usage frequency in movie scripts to their scores on movie rating sites? And with this in mind, can we translate this correlation to profitability?



There are two parts to this project:

1. Webscraping movie rating data
  - For the purpose of eliminating bias and having a (relatively) smaller dataset, we will use scores from IMDb, which is a website that compiles all rating data from all users input
  -using BeautifulSoup, request, and pandas libraries in Python
