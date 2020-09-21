# Movie Script Analyzer
A webscraping script that fetches all the movie title data for each of the 18 genres on IMDb. Specifically gets each title's rating and box office data, as well as performs sentiment analysis on the movie script using the NRC Lexicon in order to get the % of the script that expresses 10 different emotions and sentiments. 

The data is then exported to a CSV file where a correlation analysis is then done manually with each metric and the rating/box office data.

# How To Use
Just run main.py! The program will take a long time due to the sheer amount of data we are working with (200,000+ titles and each of their movie scripts), so it would be best to comment out and run one IMDb object at a time.

# References
https://www.imsdb.com/

https://monkeylearn.com/sentiment-analysis/

http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm

http://www.nltk.org/book/
