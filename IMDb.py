import requests
import random
from bs4 import BeautifulSoup
import pandas as pd


# helper function to iterate through multiple elements in an array
def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


'''
Defines the IMDb class that will contain the title and movie rating data from
# a specific genre of movies
'''
class IMDb:

    def __init__(self, name):
        self.name = name
        self.titles = []
        self.ratings = []
        self.amount = []
        self.numTitles = 0

    """ 
    main(url)
    parameters: the url of the IMDb page being looked at
    function: passes in the url ofthe IMDb page, parses all the title and
                  rating data from the url. Rating data has at least 25,000 ratings from users.
    """

    def main(self, url):
        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')

        # getting all of our necessary data from our html file
        movieTitles = soup.select('h3.lister-item-header a')
        movieRating = soup.select('div.inline-block.ratings-imdb-rating')
        grossAmount = soup.select('p.sort-num_votes-visible span[name = nv]')

        # obtain all of the necessary data needed
        self.titles.extend([title.text for title in movieTitles])
        self.ratings.extend([float(rating['data-value']) for rating in movieRating])
        # had to separate the right data values, as votes and gross amount were both under the name nv in span
        self.amount.extend(int(gross['data-value'].replace(',', '')) for votes, gross in pairwise(grossAmount))

        # print(self.titles)
        # print(self.ratings)
        # print(self.amount)

    """
        toCsv
        parameters: the list containing data points
        function: converts to csv file
    """

    def toCsv(self):
        records = []
        for (a, b, c) in zip(self.titles, self.ratings, self.amount):
            records.append((a, b, c))
        df = pd.DataFrame(records, columns=('Title', 'Rating', 'Net Gross'))
        df.to_csv(self.name + '.csv', index=False, encoding='utf-8')

    ''' 
        numberOfTitles
        parameters: url of website looked at
        function: returns number of titles of a particular genre being looked at 
    '''

    def numberOfTitles(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        numberTitles = soup.find_all("div", class_="desc")
        test = numberTitles[0].text[6:-1]
        Titles = int(''.join(filter(str.isdigit, test)))
        return Titles

    '''
        advancePages
        parameters: url of website looked at
        function: advances the pages of the particular genre until all title data is collected 
                  and stored into the private member variables of the class. 
    '''

    def advancePages(self, temp):
        # a is the temp url that is created. B is the starting number for the page
        url_pages = lambda a, b: a + '&start=' + str(b) + '&ref_=adv_nxt'

        numTitles = self.numberOfTitles(temp)
        counter = 1
        while numTitles > 50:
            counter += 50
            anew = url_pages(temp, counter)
            self.main(anew)
            numTitles -= 50
        # is there still more titles? advance one more page
        if (numTitles > 0):
            counter += 50
            anew = url_pages(temp, counter)
            self.main(anew)
        self.toCsv()

    """
    genre
    parameters: the genre currently being looked at for the ratings and title data
    function: passes in the url of the IMDb page, parses all the title and
              rating data from the url based on the any of the 18 available
              inputted genres (on the movie script website). 
    """

    def genre(self, aGenre):
        url = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres='
        # Change this based on how you want to sort the website. For now it will be based on box office, since
        # some movies actually don't have box office data.
        url_completed = '&sort=boxoffice_gross_us,desc'

        if aGenre == 'action':
            temp = url + 'action' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'adventure':
            temp = url + 'adventure' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'animation':
            temp = url + 'animation' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'comedy':
            temp = url + 'comedy' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'crime':
            temp = url + 'crime' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'drama':
            temp = url + 'drama' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'family':
            temp = url + 'family' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'fantasy':
            temp = url + 'fantasy' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'horror':
            temp = url + 'horror' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'musical':
            temp = url + 'musical' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'mystery':
            temp = url + 'mystery' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'romance':
            temp = url + 'sci-fi' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'short':
            temp = url + 'short' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'thriller':
            temp = url + 'thriller' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'war':
            temp = url + 'war' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        elif aGenre == 'western':
            temp = url + 'western' + url_completed
            self.main(temp)
            self.advancePages(temp)
            return
        else:
            return 'this genre does not exist!'
