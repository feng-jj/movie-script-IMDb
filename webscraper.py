import requests
import random
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'

# main(url)
# parameters: the url of the IMDb page being looked at
# function: passes in the url ofthe IMDb page, parses all the title and
#           rating data from the url
def main(url) :
    r = requests.get(url)

    #print(r.text[0:1000000000])

    soup  = BeautifulSoup(r.text, 'html.parser')

    #first getting all the
    movieRating = soup.select('td.ratingColumn.imdbRating')
    movieRating0 = movieRating[0]
    print(movieRating0.contents[1])

    #results = soup.find_all('tbody', attrs = {'class' : 'lister-list'})
    #print(movieRating)

    #this should equal 250 from the website
    #print(allRatings)

    for result in movieRating:
        theRating = result.find('strong').text[0:-1]
        print(theRating)

if __name__ == '__main__' :
    main(url)
