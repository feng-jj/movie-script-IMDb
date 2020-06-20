
# Defines the IMDb class that will contain the title and movie rating data from
# a specific genre of movies
class IMDb:
    titles = []
    ratings = []
    url = 'https://www.imdb.com/search/title/?genres='
    url_completed = '&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=93WCQTG7TJJFKTPNVSNT&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1'


    def __init__(self, name, titles, ratings):
        self.name = name
        self.titles = titles
        self.ratings = ratings

    # main(url)
    # parameters: the url of the IMDb page being looked at
    # function: passes in the url ofthe IMDb page, parses all the title and
    #           rating data from the url
    def main(url) :
        r = requests.get(url)

        soup  = BeautifulSoup(r.text, 'html.parser')

        #getting all of our necessary data
        movieRating = soup.select('td.posterColumn span[name = ir]')
        movieTitles = soup.select('td.titleColumn a')

        #obtain all of the necessary data needed
        titles = [title.text for title in movieTitles]
        ratings = [float(rating['data-value']) for rating in movieRating]

        #only uncomment for testing purposes
        #print(titles)
        #print(ratings)

    # genre(url)
    # parameters: the genre currently being looked at for the ratings and title data
    # function: passes in the url ofthe IMDb page, parses all the title and
    #           rating data from the url based on the any of the 18 available
    #           inputted genres (on the movie script website)
    def genre(aGenre):
        switch(aGenre):
            case 'action' :
                temp = url + 'action' + url_completed
                main(url_completed)
                return
            case 'adventure' :
                temp = url + 'adventure' + url_completed
                main(url_completed)
                return
            case 'animation' :
                temp = url + 'animation' + url_completed
                main(url_completed)
                return
            case 'comedy' :
                temp = url + 'comedy' + url_completed
                main(url_completed)
                return
            case 'crime' :
                temp = url + 'crime' + url_completed
                main(url_completed)
                return
            case 'drama' :
                temp = url + 'drama' + url_completed
                main(url_completed)
                return
            case 'family' :
                temp = url + 'family' + url_completed
                main(url_completed)
                return
            case 'fantasy' :
                temp = url + 'fantasy' + url_completed
                main(url_completed)
                return
            case 'horror' :
                temp = url + 'horror' + url_completed
                main(url_completed)
                return
            case 'musical' :
                temp = url + 'musical' + url_completed
                main(url_completed)
                return
            case 'mystery' :
                temp = url + 'mystery' + url_completed
                main(url_completed)
                return
            case 'romance' :
                temp = url + 'sci-fi' + url_completed
                main(url_completed)
                return
            case 'short' :
                temp = url + 'short' + url_completed
                main(url_completed)
                return
            case 'thriller' :
                temp = url + 'thriller' + url_completed
                main(url_completed)
                return
            case 'war' :
                temp = url + 'war' + url_completed
                main(url_completed)
                return
            case 'western' :
                temp = url + 'western' + url_completed
                main(url_completed)
                return
