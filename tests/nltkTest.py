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
'''
    This file is used to test natural language processing
'''

url = 'https://www.imsdb.com/scripts/'

def toUrl(title) :
    urlTitle = title
    if ':' in title:
        urlTitle = urlTitle.replace(':', '')
    if title[0:3] == 'The':
        urlTitle = urlTitle.replace('The ', '')
        urlTitle += ',-The'
    urlTitle = urlTitle.replace(" ", "-")
    return url + urlTitle + '.html'

"""
    Separates the url containing the script into a pair with dialogue and titles (i.e. names of characters, camera
    movement instructions such as FADE IN)
"""

def getCorp(title):
    urls = toUrl(title)
    r = requests.get(urls)
    soup = BeautifulSoup(r.text, 'html.parser')

    # want to separate the titles (i.e. character names) with the dialogue.
    corpora = soup.find_all("pre")
    title_info = soup.find_all("b")

    if (corpora == "") :
        return {"", ""}

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
    This method utilizes the NRCLex library that processes the emotional counts
    of the movie script.
"""
def emotions(script) :
    totalScript = script[0] + script[1]
    text_object = NRCLex(totalScript);
    #Return words list.

    text_object.words

    #Return sentences list.

    text_object.sentences

    #Return affect list.

    text_object.affect_list

    #Return affect dictionary.

    text_object.affect_dict

    #Return raw emotional counts. This one gives the actual frequency
    #of each emotion

    print(text_object.raw_emotion_scores)

    #Return highest emotions.

    print(text_object.top_emotions)

    print(text_object.affect_frequencies)

    frequencies = text_object.affect_frequencies

    SUM = list(frequencies.values())

    return SUM

"""
    Testing the TextBlob lexicon
"""
def blob(script) :
    blob_object = TextBlob(script);

    print(blob_object.sentiment)


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
    stop_words.extend(update_list)

    words = word_tokenize(fullScript)
    # extracting only the dialogue and plot descriptions
    filtered_text = [w for w in words if not w in stop_words and not w in titles1]

    # this part tags the part of speech of each word inside the movie script
    #tagged_text = pos_tag(filtered_text)
    #print(tagged_text)
    return filtered_text


if __name__ == '__main__':
    newUrl = "Blade: Trinity"
    print(newUrl[0:2])
    info = getCorp(newUrl)
    script_words = token(info[0], info[1])
    freq_dist = FreqDist(script_words)
    stuff = emotions(info)
    print(stuff[0])
    stuff1 = blob(info[0] + info[1])
    #print(stuff)
