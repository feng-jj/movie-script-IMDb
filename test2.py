import nltk
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import pos_tag
from nltk import FreqDist
'''
    This file is used to test natural language processing
'''

url = 'https://www.imsdb.com/scripts/Good-Will-Hunting.html'



"""
    Separates the url containing the script into a pair with dialogue and titles (i.e. names of characters, camera
    movement instructions such as FADE IN)
"""

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

    pair = (fullScript, allTitles)

    return pair


"""
    This is used to tag the part of speech that each word is in the movie script
"""
def token(fullScript, allTitles) :
    # titles1 contains all the things we want to separate from the dialogue
    titles1 = word_tokenize(allTitles)

    # first extending all of the title and setting descriptions to the list of stop words
    stop_words = [stopwords.words("english")]
    stop_words.extend(titles1)
    update_list = ['the', 'and', 'you']
    #stop_words.extend('to', 'the')

    words = word_tokenize(fullScript)
    # extracting only the dialogue and plot descriptions
    filtered_text = [w for w in words if not w in stop_words and not w in titles1]

    # this part tags the part of speech of each word inside the movie script
    tagged_text = pos_tag(filtered_text)
    #print(tagged_text)
    return filtered_text




if __name__ == '__main__':
    info = getCorp(url)
    script_words = token(info[0], info[1])
    freq_dist = FreqDist(script_words)
    print(freq_dist.most_common(100))
