import requests
import random
from IMDb import IMDb
from bs4 import BeautifulSoup


if __name__ == '__main__' :
    horror = IMDb("animation movies")
    horror.genre('animation')
    # print(horror.titles)
    # print(horror.ratings)
