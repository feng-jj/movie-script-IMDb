import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import PunktSentenceTokenizer

'''
    This file is used to test natural language processing 
'''

url = 'https://www.imsdb.com/scripts/Good-Will-Hunting.html'


def getCorp(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # want to separate the titles (i.e. character names) with the dialogue.
    corpora = soup.find_all("pre")
    title_info = soup.find_all("b")

    # extracting our text
    # script contains the dialogue and scenic descriptions in the script. The Titles contains title,
    # name, camera movement, and setting descriptions. This way we can process dialogue separately
    script = [w for w in corpora]
    titles = [names.text for names in title_info]

    # contains the dialogue of our script
    fullScript = ''
    allTitles = ''

    for x in range(0, len(script)):
        # print(script[x].text)
        fullScript += (script[x].text)

    for y in range(0, len(titles)):
        allTitles += titles[y]

    # exploring tagging parts of speech

    tokenized = PunktSentenceTokenizer

    for i in fullScript :
        words = nltk


    # # titles1 contains all the things we want to separate from the dialogue
    # titles1 = word_tokenize(allTitles)
    #
    # #first extending all of the title and setting descriptions
    # stop_words = [stopwords.words("english")]
    # stop_words.extend(titles1)
    # words = word_tokenize(fullScript)
    #
    # # extracting only the dialogue and plot descriptions
    # filtered_text = [w for w in words if not w in stop_words and not w in titles1]
    # print(filtered_text)


if __name__ == '__main__':
    getCorp(url)
