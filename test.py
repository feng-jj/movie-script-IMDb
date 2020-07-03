import requests
import random
from IMDb import IMDb
from bs4 import BeautifulSoup
import pandas as pd

""" 
    This file is used to test out functionality and new added features.
"""
#url = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=animation&sort=boxoffice_gross_us,desc'


titles = []
ratings = []
amount = []

def genre(aGenre):
    url = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres='
    # Change this based on how you want to sort the website. For now it will be based on box office, since
    # some movies actually don't have box office data.
    url_completed = '&sort=boxoffice_gross_us,desc'

    # a is the temp url that is created. b is the starting number for the page
    url_pages = lambda a, b: a + '&start=' + str(b) + '&ref_=adv_nxt'

    #if aGenre == 'action':
    temp = url + 'action' + url_completed
    main(temp)
    numTitles = numberOfTitles(temp)
    counter = 1
    while numTitles > 50:
        counter += 50
        anew = url_pages(temp, counter)
        main(anew)
        numTitles -= 50
    if (numTitles > 0) :
        counter += 50
        anew = url_pages(temp, counter)
        main(anew)
    return

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
    titles.extend([title.text for title in movieTitles])
    ratings.extend([float(rating['data-value']) for rating in movieRating])
    # had to separate the right data values, as votes and gross amount were both under the name nv in span
    amount.extend(int(gross['data-value'].replace(',', '')) for votes, gross in pairwise(grossAmount))

    #print(numTitles)

    # records = []
    # for (a, b, c) in zip(titles, ratings, amount):
    #     records.append((a, b, c))
    #
    # df = pd.DataFrame(records, columns=('Title', 'Rating', 'Net Gross'))
    # df.head()
    # df.tail()
    # df.to_csv('theData.csv', index=False, encoding='utf-8')

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def numberOfTitles(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    numberTitles = soup.find_all("div", class_="desc")
    test = numberTitles[0].text[6:-1]
    Titles = int(''.join(filter(str.isdigit, test)))
    return Titles
    #numTitles = numbTitles[0]

if __name__ == '__main__' :
    genre('action')
    print(titles)
    print(ratings)
    print(amount)
    print(len(titles))
