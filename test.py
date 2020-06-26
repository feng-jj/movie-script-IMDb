import requests
import random
from IMDb import IMDb
from bs4 import BeautifulSoup
import pandas as pd

""" 
    This file is used to test out functionality and new added features.
"""

url = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=horror&sort=user_rating,desc'
def main(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    # getting all of our necessary data
    # movieRating = soup.select('div.inline-block.ratings-imdb-rating')
    # theRating = movieRating.find('strong').text
    movieTitles = soup.select('h3.lister-item-header a')
    movieRating = soup.select('div.inline-block.ratings-imdb-rating')
    grossAmount = soup.select('p.sort-num_votes-visible span[name = nv]')
    # obtain all of the necessary data needed
    titles = [title.text for title in movieTitles]
    ratings = [float(rating['data-value']) for rating in movieRating]
    amount = [int(gross['data-value'].replace(',', '')) for gross in grossAmount]

    print(titles)
    print(ratings)
    print(amount)

    records = []
    for (a, b, c) in zip(titles, ratings, amount):
        records.append((a, b, c))

    df = pd.DataFrame(records, columns=('Title', 'Rating', 'Net Gross'))
    df.head()
    df.tail()
    df.to_csv('theData.csv', index=False, encoding='utf-8')


if __name__ == '__main__' :
    main(url)
