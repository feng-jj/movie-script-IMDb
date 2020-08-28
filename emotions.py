import nltk
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import pos_tag
from nltk import FreqDist
from nrclex import NRCLex
from textblob import TextBlob


class emotions:
    '''
        Emotions class object. Contains analyzed corpora information for all
        movie scripts from most of titles from genre, as listed by IMDb.
        Limitations due to lack of access for certain scripts, data is excluded
        for those.
    '''
    def __init__(self, titles, genre):
        self.genre = genre
        self.titles = titles
        self.url ='https://www.imsdb.com/scripts/'
        self.polarity = []
        self.subjectivity = []
        self.positive = []
        self.negative = []
        self.fear = []
        self.anticipation = []
        self.sadness = []
        self.anger = []
        self.disgust = []
        self.joy = []
        self.trust = []
        self.surprise = []
        self.getEmotions()

    '''
        Populates our class with all the movie titles' emotion data in their
        respective catagories.
    '''
    def getEmotions(self) :
        for title in self.titles :
            htmlUrl = self.toUrl(title)
            corp = self.getCorp(htmlUrl)
            if (corp == {"", ""}):
                self.polarity.append(None)
                self.subjectivity.append(None)
                self.positive.append(None)
                self.negative.append(None)
                self.fear.append(None)
                self.anticipation.append(None)
                self.sadness.append(None)
                self.anger.append(None)
                self.disgust.append(None)
                self.joy.append(None)
                self.trust.append(None)
                self.surprise.append(None)
                continue
            else:
                self.populateEmotions(corp)

    '''
        Separates the url containing the script into a pair with dialogue and titles
        (i.e. names of characters, camera movement instructions such as FADE IN)
    '''

    def getCorp(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        # want to separate the titles (i.e. character names) with the dialogue.
        corpora = soup.find_all("pre")
        title_info = soup.find_all("b")

        if (corpora == "") :
            return {"", ""}

        # extracting our text
        # script contains the dialogue and scenic descriptions. Titles contain
        # stage directions and character names.
        script = [w for w in corpora]
        titles = [names.text for names in title_info]

        fullScript = ''
        allTitles = ''

        for x in range(0, len(script)):
            # print(script[x].text)
            fullScript += (script[x].text)

        for y in range(0, len(titles)):
            allTitles += titles[y]

        pair = (fullScript, allTitles)

        return pair

    '''
        Populating the stuctures inside our class with emotion statistics
    '''
    def populateEmotions(self, script) :
        totalScript = script[0] + script[1]
        text_object = NRCLex(totalScript)
        #emotion_scores = text_object.raw_emotion_scores
        frequency_of_emotions = list(text_object.affect_frequencies.values())
        self.fear.append(frequency_of_emotions[0])
        self.anger.append(frequency_of_emotions[1])
        self.anticipation.append(frequency_of_emotions[2])
        self.trust.append(frequency_of_emotions[3])
        self.surprise.append(frequency_of_emotions[4])
        self.positive.append(frequency_of_emotions[5])
        self.negative.append(frequency_of_emotions[6])
        self.sadness.append(frequency_of_emotions[7])
        self.disgust.append(frequency_of_emotions[8])
        self.joy.append(frequency_of_emotions[9])
        # getting polarity and subjectivity
        blob_object = TextBlob(totalScript)
        sentiments = list(blob_object.sentiment)
        self.polarity.append(sentiments[0])
        self.subjectivity.append(sentiments[1])

    '''
        Converting the title into the proper URL on the IMDSb website
    '''
    def toUrl(self, title) :
        urlTitle = title
        # preprocessing the format of the html link
        if ' - ' in title:
            urlTitle = urlTitle.replace(' - ', ' ')
        if ':' in title:
            urlTitle = urlTitle.replace(':', '')
        if title[0:4] == 'The ':
            urlTitle.replace(title[0:4], '')
            urlTitle += ',-The'
        # replace all spaces with dashes '-'
        urlTitle = urlTitle.replace(' ', '-')
        return self.url + urlTitle + '.html'
