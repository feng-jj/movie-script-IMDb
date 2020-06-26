import requests
import random
from bs4 import BeautifulSoup
import pandas as pd

# Defines the IMDb class that will contain the title and movie rating data from
# a specelific genre of movies
class IMDb:

    def __init__(self, name):
        self.name = name
        self.titles = []
        self.ratings = []
        self.amount = []

    """ 
    main(url)
    parameters: the url of the IMDb page being looked at
    function: passes in the url ofthe IMDb page, parses all the title and
                  rating data from the url
    """
    def main(self, url) :
        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')

        # getting all of our necessary data from our html file
        movieTitles = soup.select('h3.lister-item-header a')
        movieRating = soup.select('div.inline-block.ratings-imdb-rating')
        grossAmount = soup.select('p.sort-num_votes-visible span[name = nv]')

        # obtain all of the necessary data needed
        self.titles = [title.text for title in movieTitles]
        self.ratings = [float(rating['data-value']) for rating in movieRating]
        self.amount = [int(gross['data-value'].replace(',', '')) for gross in grossAmount]

        print(self.titles)
        print(self.ratings)
        print(self.amount)

        records = []
        for (a, b, c) in zip(self.titles, self.ratings, self.amount):
            records.append((a, b, c))

        #parses all of our data from our three lists of data
        df = pd.DataFrame(records, columns=('Title', 'Rating', 'Net Gross'))
        # df.head()
        # df.tail()
        df.to_csv(self.name + '.csv', index=False, encoding='utf-8')
    """
    genre(aGenre)
    parameters: the genre currently being looked at for the ratings and title data
    function: passes in the url of the IMDb page, parses all the title and
              rating data from the url based on the any of the 18 available
              inputted genres (on the movie script website)
    """
    def genre(self, aGenre):
        url = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres='
        url_completed = '&sort=user_rating,desc'
        if aGenre == 'action':
            temp = url + 'action' + url_completed
            self.main(temp)
            return
        elif aGenre == 'adventure' :
            temp = url + 'adventure' + url_completed
            self.main(temp)
            return
        elif aGenre =='animation' :
            temp = url + 'animation' + url_completed
            self.main(temp)
            return
        elif aGenre =='comedy' :
            temp = url + 'comedy' + url_completed
            self.main(temp)
            return
        elif aGenre =='crime' :
            temp = url + 'crime' + url_completed
            self.main(temp)
            return
        elif aGenre == 'drama' :
            temp = url + 'drama' + url_completed
            self.main(temp)
            return
        elif aGenre =='family' :
            temp = url + 'family' + url_completed
            self.main(temp)
            return
        elif aGenre =='fantasy' :
            temp = url + 'fantasy' + url_completed
            self.main(temp)
            return
        elif aGenre =='horror' :
            temp = url + 'horror' + url_completed
            self.main(temp)
            return
        elif aGenre =='musical' :
            temp = url + 'musical' + url_completed
            self.main(temp)
            return
        elif aGenre =='mystery' :
            temp = url + 'mystery' + url_completed
            self.main(temp)
            return
        elif aGenre =='romance' :
            temp = url + 'sci-fi' + url_completed
            self.main(temp)
            return
        elif aGenre =='short' :
            temp = url + 'short' + url_completed
            self.main(temp)
            return
        elif aGenre =='thriller' :
            temp = url + 'thriller' + url_completed
            self.main(temp)
            return
        elif aGenre =='war' :
            temp = url + 'war' + url_completed
            self.main(temp)
            return
        elif aGenre =='western' :
            temp = url + 'western' + url_completed
            self.main(temp)
            return
